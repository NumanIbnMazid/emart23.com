import random
import string
import time
from django.utils.text import slugify
from urllib.parse import urlparse
from django.db import models
from django.dispatch import receiver
import uuid


def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    """[Generates random string]

    Args:
        size (int, optional): [size of string to generate]. Defaults to 4.
        chars ([str], optional): [characters to use]. Defaults to string.ascii_lowercase+string.digits.

    Returns:
        [str]: [Generated random string]
    """
    return ''.join(random.choice(chars) for _ in range(size))


def random_number_generator(size=4, chars='1234567890'):
    """[Generates random number]

    Args:
        size (int, optional): [size of number to generate]. Defaults to 4.
        chars (str, optional): [numbers to use]. Defaults to '1234567890'.

    Returns:
        [str]: [Generated random number]
    """
    return ''.join(random.choice(chars) for _ in range(size))


def simple_random_string():
    """[Generates simple random string]

    Returns:
        [str]: [Generated random string]
    """
    timestamp_m = time.strftime("%Y")
    timestamp_d = time.strftime("%m")
    timestamp_y = time.strftime("%d")
    timestamp_now = time.strftime("%H%M%S")
    random_str = random_string_generator()
    random_num = random_number_generator()
    bindings = (
        random_str + timestamp_d + random_num + timestamp_now +
        timestamp_y + random_num + timestamp_m
    )
    return bindings


def simple_random_string_with_timestamp(size=None):
    """[Generates random string with timestamp]

    Args:
        size ([int], optional): [Size of string]. Defaults to None.

    Returns:
        [str]: [Generated random string]
    """
    timestamp_m = time.strftime("%Y")
    timestamp_d = time.strftime("%m")
    timestamp_y = time.strftime("%d")
    random_str = random_string_generator()
    random_num = random_number_generator()
    bindings = (
        random_str + timestamp_d + timestamp_m + timestamp_y + random_num
    )
    if not size == None:
        return bindings[0:size]
    return bindings


def unique_slug_generator(instance, field=None, new_slug=None):
    """[Generates unique slug]

    Args:
        instance ([Model Class instance]): [Django Model class object instance].
        field ([Django Model Field], optional): [Django Model Class Field]. Defaults to None.
        new_slug ([str], optional): [passed new slug]. Defaults to None.

    Returns:
        [str]: [Generated unique slug]
    """
    if field == None:
        field = instance.title
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(field[:50])

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def url_check(url):
    """[Checks if a provided string is URL or Not]

    Args:
        url ([str]): [URL String]

    Returns:
        [bool]: [returns True if provided string is URL, otherwise returns False]
    """

    min_attr = ('scheme', 'netloc')

    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except:
        return False


def autoslugFromField(fieldname):
    """[Generates auto slug from model's field value]

    Args:
        fieldname ([str]): [Model field name to use to generate slug]
    """
    
    def decorator(model):
        # some sanity checks first
        assert hasattr(model, fieldname), f"Model has no field {fieldname!r}"
        assert hasattr(model, "slug"), "Model is missing a slug field"

        @receiver(models.signals.pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, raw=False, **kwargs):
            if not raw and not instance.slug:
                source = getattr(instance, fieldname)
                try:
                    slug = slugify(source)
                    Klass = instance.__class__
                    qs_exists = Klass.objects.filter(slug=slug).exists()
                    if qs_exists:
                        new_slug = "{slug}-{randstr}".format(
                            slug=slug,
                            randstr=random_string_generator(size=4)
                        )
                        instance.slug = new_slug
                    else:
                        instance.slug = slug
                except Exception as e:
                    instance.slug = simple_random_string()
        return model
    return decorator
        

def autoslugFromUUID():
    """[Generates auto slug using UUID]
    """
    
    def decorator(model):
        assert hasattr(model, "slug"), "Model is missing a slug field"

        @receiver(models.signals.pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, raw=False, **kwargs):
            if not raw and not instance.slug:
                try:
                    instance.slug = str(uuid.uuid4())
                except Exception as e:
                    instance.slug = simple_random_string()
        return model
    return decorator


def generate_unique_username_from_email(instance):
    """[Generates unique username from email]

    Args:
        instance ([model class object instance]): [model class object instance]

    Raises:
        ValueError: [If found invalid email]

    Returns:
        [str]: [unique username]
    """

    # get email from instance
    email = instance.email

    if not email:
        raise ValueError("Invalid email!")

    def generate_username(email):
        return email.split("@")[0][:15] + "__" + simple_random_string_with_timestamp(size=5)

    generated_username = generate_username(email=email)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(username=generated_username).exists()

    if qs_exists:
        # recursive call
        generate_unique_username_from_email(instance=instance)

    return generated_username

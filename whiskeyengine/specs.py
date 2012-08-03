from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb(processors.Resize):
    width = 80
    height = 80
    #crop = False
    crop = True

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 160

# now lets create an adjustment processor to enhance the image at small sizes
class EnhanceThumb(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

# now we can define our thumbnail spec
class Thumbnail(ImageSpec):
    access_as = 'thumbnail_image'
    pre_cache = True
    processors = [ResizeThumb, EnhanceThumb]

# and our display spec
class Display(ImageSpec):
    pre_cache = True
    processors = [ResizeDisplay]

# extra sizes for home page rated, reviewed
class ResizeRated(processors.Resize):
    width = 110
    height = 160
    crop = False

class ResizeReviewed(processors.Resize):
    width = 38
    height = 58
    crop = False

class Rated(ImageSpec):
    pre_cache = True
    processors = [ResizeRated]

class Reviewed(ImageSpec):
    pre_cache = True
    processors = [ResizeReviewed, EnhanceThumb]

class ResizeFeatured(processors.Resize):
    width = 258
    height = 389

class Featured(ImageSpec):
    pre_cache = True
    processors = [ResizeFeatured]

class ResizeCategory(processors.Resize):
    width = 64
    height = 96
    crop = True

class Category(ImageSpec):
    access_as = 'category_image'
    pre_cache = True
    processors = [ResizeCategory]

class ResizeReviewAvatar(processors.Resize):
    width = 38
    height = 38
    crop = True

class ReviewAvatar(ImageSpec):
    access_as = 'review_avatar'
    pre_cache = True
    processors = [ResizeReviewAvatar, EnhanceThumb]

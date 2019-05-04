import config

ma = config.ma

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','price', 'image')

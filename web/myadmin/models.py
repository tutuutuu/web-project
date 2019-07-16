from django.db import models

# Create your models here.

# 用户模型
class User(models.Model):
	# 用户名
	username = models.CharField(max_length=20, null=True)
	# 密码
	password = models.CharField(max_length=77)
	# 电话
	phone = models.CharField(max_length=11)
	# 邮箱
	email = models.CharField(max_length=100)
	# 年龄
	age = models.IntegerField(null=True)
	# 照片
	pic_url = models.CharField(max_length=100)
	# 性别选择
	SEX_CHOICES = (
		(0, '女'),
		(1, '男'),
	)
	sex = models.CharField(max_length=1,null=True,choices=SEX_CHOICES)
	# 状态  0：可用   1：拉黑
	status = models.IntegerField(default=0)
	# 添加时间
	addtime = models.DateTimeField(auto_now_add=True)


# 商品分类模型
class Cates(models.Model):
	# 分类名称
	name = models.CharField(max_length=20)
	# 父级id
	pid = models.IntegerField()
	# 先辈级id
	path = models.CharField(max_length=50)

	'''
	id   name   pid   path
	1    服装   0     0,
	2    男装   1     0,1,
	3    女装   1     0,1
	4    西服   2     0,1,2
	'''



# 商品模型
class Goods(models.Model):
	# 所属分类id   分类表的外键
	cateid = models.ForeignKey(to="Cates", to_field="id")
	# 商品名称
	goodsname = models.CharField(max_length=50)
	# 商品标题
	title = models.CharField(max_length=255)
	# 商品价格
	price = models.FloatField()
	# 商品数量
	goodsnum = models.IntegerField()
	# 商品图片
	pic_url = models.CharField(max_length=255)
	# 商品详情
	goodsinfo = models.TextField()
	# 商品销量
	ordernum = models.IntegerField(default=0)
	# 点击次数
	clicknum = models.IntegerField(default=0)
	# 商品状态   0:热卖   1:下架
	status = models.IntegerField(default=0)
	# 添加时间
	addtime = models.DateTimeField(auto_now_add=True)





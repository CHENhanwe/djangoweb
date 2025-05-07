#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime


class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False,unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False,unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False,unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False,unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品表名' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    buynumber=models.IntegerField ( null=False, unique=False,default='0', verbose_name='购买数量' )
    price=models.FloatField ( null=True, unique=False,default='0', verbose_name='单价' )
    discountprice=models.FloatField ( null=True, unique=False,default='0', verbose_name='会员价' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField ( null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField ( null=True, unique=False, verbose_name='提问' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField ( null=True, unique=False,default='0', verbose_name='是否回复' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '客服聊天表'
class chongwufenlei(BaseModel):
    __doc__ = u'''chongwufenlei'''
    __tablename__ = 'chongwufenlei'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='分类' )
    '''
    fenlei=VARCHAR
    '''
    class Meta:
        db_table = 'chongwufenlei'
        verbose_name = verbose_name_plural = '宠物分类'
class chongwuguashi(BaseModel):
    __doc__ = u'''chongwuguashi'''
    __tablename__ = 'chongwuguashi'


    __authTables__={'yonghuming':'yonghu'}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    guashibiaoti=models.CharField ( max_length=255,null=False,unique=False, verbose_name='挂失标题' )
    fenlei=models.CharField ( max_length=255,null=False,unique=False, verbose_name='分类' )
    chongwumingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='宠物名称' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    chengshi=models.CharField ( max_length=255,null=True,unique=False, verbose_name='城市' )
    yishididian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='遗失地点' )
    yishishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='遗失时间' )
    faburiqi=models.DateField ( null=True, unique=False, verbose_name='发布日期' )
    neirongxiangqing=models.TextField ( null=True, unique=False, verbose_name='内容详情' )
    yonghuming=models.CharField ( max_length=255,null=True,unique=False, verbose_name='用户名' )
    shouji=models.CharField ( max_length=255,null=True,unique=False, verbose_name='手机' )
    '''
    guashibiaoti=VARCHAR
    fenlei=VARCHAR
    chongwumingcheng=VARCHAR
    tupian=VARCHAR
    chengshi=VARCHAR
    yishididian=VARCHAR
    yishishijian=DateTime
    faburiqi=Date
    neirongxiangqing=Text
    yonghuming=VARCHAR
    shouji=VARCHAR
    '''
    class Meta:
        db_table = 'chongwuguashi'
        verbose_name = verbose_name_plural = '宠物挂失'
class chongwujicun(BaseModel):
    __doc__ = u'''chongwujicun'''
    __tablename__ = 'chongwujicun'


    __authTables__={'yonghuming':'yonghu'}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jicunbiaoti=models.CharField ( max_length=255,null=False,unique=False, verbose_name='寄存标题' )
    chongwumingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='宠物名称' )
    fenlei=models.CharField ( max_length=255,null=True,unique=False, verbose_name='分类' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    xingbie=models.CharField ( max_length=255,null=True,unique=False, verbose_name='性别' )
    nianling=models.CharField ( max_length=255,null=True,unique=False, verbose_name='年龄' )
    jicunneirong=models.TextField ( null=True, unique=False, verbose_name='寄存内容' )
    shangdianbianhao=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商店编号' )
    shangdianmingcheng=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商店名称' )
    lianxidianhua=models.CharField ( max_length=255,null=True,unique=False, verbose_name='联系电话' )
    jicunriqi=models.DateField ( null=True, unique=False, verbose_name='寄存日期' )
    beizhu=models.CharField ( max_length=255,null=True,unique=False, verbose_name='备注' )
    yonghuming=models.CharField ( max_length=255,null=True,unique=False, verbose_name='用户名' )
    shouji=models.CharField ( max_length=255,null=True,unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255,null=True,unique=False, verbose_name='是否审核' )
    shhf=models.TextField ( null=True, unique=False, verbose_name='审核回复' )
    '''
    jicunbiaoti=VARCHAR
    chongwumingcheng=VARCHAR
    fenlei=VARCHAR
    tupian=VARCHAR
    xingbie=VARCHAR
    nianling=VARCHAR
    jicunneirong=Text
    shangdianbianhao=VARCHAR
    shangdianmingcheng=VARCHAR
    lianxidianhua=VARCHAR
    jicunriqi=Date
    beizhu=VARCHAR
    yonghuming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'chongwujicun'
        verbose_name = verbose_name_plural = '宠物寄存'
class chongwulingyang(BaseModel):
    __doc__ = u'''chongwulingyang'''
    __tablename__ = 'chongwulingyang'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chongwumingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='宠物名称' )
    fenlei=models.CharField ( max_length=255,null=False,unique=False, verbose_name='分类' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    zhonglei=models.CharField ( max_length=255,null=False,unique=False, verbose_name='种类' )
    nianling=models.CharField ( max_length=255,null=True,unique=False, verbose_name='年龄' )
    xingbie=models.CharField ( max_length=255,null=True,unique=False, verbose_name='性别' )
    xingqing=models.CharField ( max_length=255,null=True,unique=False, verbose_name='性情' )
    chongwuzhuangtai=models.CharField ( max_length=255,null=True,unique=False, verbose_name='宠物状态' )
    yimiaoqingkuang=models.CharField ( max_length=255,null=True,unique=False, verbose_name='疫苗情况' )
    lingyangfeiyong=models.IntegerField ( null=False, unique=False,default='0', verbose_name='领养费用' )
    lingyangshuoming=models.TextField ( null=True, unique=False, verbose_name='领养说明' )
    '''
    chongwumingcheng=VARCHAR
    fenlei=VARCHAR
    tupian=VARCHAR
    zhonglei=VARCHAR
    nianling=VARCHAR
    xingbie=VARCHAR
    xingqing=VARCHAR
    chongwuzhuangtai=VARCHAR
    yimiaoqingkuang=VARCHAR
    lingyangfeiyong=Integer
    lingyangshuoming=Text
    '''
    class Meta:
        db_table = 'chongwulingyang'
        verbose_name = verbose_name_plural = '宠物领养'
class chongwushangdian(BaseModel):
    __doc__ = u'''chongwushangdian'''
    __tablename__ = 'chongwushangdian'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangdianbianhao=models.CharField ( max_length=255,null=False,unique=False, verbose_name='商店编号' )
    shangdianmingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='商店名称' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    jingyingfanwei=models.CharField ( max_length=255,null=True,unique=False, verbose_name='经营范围' )
    lianxiren=models.CharField ( max_length=255,null=True,unique=False, verbose_name='联系人' )
    lianxidianhua=models.CharField ( max_length=255,null=True,unique=False, verbose_name='联系电话' )
    shangdiandizhi=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商店地址' )
    shangdianjieshao=models.TextField ( null=True, unique=False, verbose_name='商店介绍' )
    '''
    shangdianbianhao=VARCHAR
    shangdianmingcheng=VARCHAR
    tupian=VARCHAR
    jingyingfanwei=VARCHAR
    lianxiren=VARCHAR
    lianxidianhua=VARCHAR
    shangdiandizhi=VARCHAR
    shangdianjieshao=Text
    '''
    class Meta:
        db_table = 'chongwushangdian'
        verbose_name = verbose_name_plural = '宠物商店'
class chongwuyongpin(BaseModel):
    __doc__ = u'''chongwuyongpin'''
    __tablename__ = 'chongwuyongpin'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='商品名称' )
    fenlei=models.CharField ( max_length=255,null=True,unique=False, verbose_name='分类' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    guige=models.CharField ( max_length=255,null=True,unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255,null=True,unique=False, verbose_name='品牌' )
    baozhiqi=models.CharField ( max_length=255,null=True,unique=False, verbose_name='保质期' )
    shangpinxiangqing=models.TextField ( null=True, unique=False, verbose_name='商品详情' )
    shengchanriqi=models.DateField ( null=True, unique=False, verbose_name='生产日期' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField ( null=True, unique=False,default='0', verbose_name='点击次数' )
    price=models.FloatField ( null=False, unique=False,default='0', verbose_name='价格' )
    '''
    shangpinmingcheng=VARCHAR
    fenlei=VARCHAR
    tupian=VARCHAR
    guige=VARCHAR
    pinpai=VARCHAR
    baozhiqi=VARCHAR
    shangpinxiangqing=Text
    shengchanriqi=Date
    clicktime=DateTime
    clicknum=Integer
    price=Float
    '''
    class Meta:
        db_table = 'chongwuyongpin'
        verbose_name = verbose_name_plural = '宠物用品'
class discusschongwuguashi(BaseModel):
    __doc__ = u'''discusschongwuguashi'''
    __tablename__ = 'discusschongwuguashi'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    content=models.TextField ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusschongwuguashi'
        verbose_name = verbose_name_plural = '宠物挂失评论表'
class discusschongwulingyang(BaseModel):
    __doc__ = u'''discusschongwulingyang'''
    __tablename__ = 'discusschongwulingyang'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    content=models.TextField ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusschongwulingyang'
        verbose_name = verbose_name_plural = '宠物领养评论表'
class discusschongwushangdian(BaseModel):
    __doc__ = u'''discusschongwushangdian'''
    __tablename__ = 'discusschongwushangdian'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    content=models.TextField ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusschongwushangdian'
        verbose_name = verbose_name_plural = '宠物商店评论表'
class discusschongwuyongpin(BaseModel):
    __doc__ = u'''discusschongwuyongpin'''
    __tablename__ = 'discusschongwuyongpin'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    content=models.TextField ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusschongwuyongpin'
        verbose_name = verbose_name_plural = '宠物用品评论表'
class forum(BaseModel):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=True,unique=False, verbose_name='帖子标题' )
    content=models.TextField ( null=False, unique=False, verbose_name='帖子内容' )
    parentid=models.BigIntegerField ( null=True, unique=False, verbose_name='父节点id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255,null=True,unique=False, verbose_name='用户名' )
    isdone=models.CharField ( max_length=255,null=True,unique=False, verbose_name='状态' )
    '''
    title=VARCHAR
    content=Text
    parentid=BigInteger
    userid=BigInteger
    username=VARCHAR
    isdone=VARCHAR
    '''
    class Meta:
        db_table = 'forum'
        verbose_name = verbose_name_plural = '论坛表'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False,unique=False, verbose_name='标题' )
    picture=models.CharField ( max_length=255,null=False,unique=False, verbose_name='图片' )
    content=models.TextField ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '宠物资讯'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品表名' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField ( null=False, unique=False,default='0', verbose_name='购买数量' )
    price=models.FloatField ( null=False, unique=False,default='0', verbose_name='价格/积分' )
    discountprice=models.FloatField ( null=True, unique=False,default='0', verbose_name='折扣价格' )
    total=models.FloatField ( null=False, unique=False,default='0', verbose_name='总价格/总积分' )
    discounttotal=models.FloatField ( null=True, unique=False,default='0', verbose_name='折扣总价格' )
    type=models.IntegerField ( null=True, unique=False,default='0', verbose_name='支付类型' )
    status=models.CharField ( max_length=255,null=True,unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255,null=True,unique=False, verbose_name='地址' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    total=Float
    discounttotal=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class shangpinfenlei(BaseModel):
    __doc__ = u'''shangpinfenlei'''
    __tablename__ = 'shangpinfenlei'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='分类' )
    '''
    fenlei=VARCHAR
    '''
    class Meta:
        db_table = 'shangpinfenlei'
        verbose_name = verbose_name_plural = '商品分类'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'


    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField ( null=True, unique=False, verbose_name='收藏id' )
    tablename=models.CharField ( max_length=255,null=True,unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False,unique=False, verbose_name='收藏名称' )
    picture=models.CharField ( max_length=255,null=False,unique=False, verbose_name='收藏图片' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'
    __loginUser__ = 'yonghuming'

    __authTables__={}
    __authPeople__ = '是'  # 用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__ = 'yonghuming'  # 用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuming=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户名' )
    mima=models.CharField ( max_length=255,null=False,unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False,unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255,null=True,unique=False, verbose_name='性别' )
    touxiang=models.CharField ( max_length=255,null=True,unique=False, verbose_name='头像' )
    shouji=models.CharField ( max_length=255,null=True,unique=False, verbose_name='手机' )
    money=models.FloatField ( null=True, unique=False,default='0', verbose_name='余额' )
    '''
    yonghuming=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=VARCHAR
    shouji=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class yonghulingyang(BaseModel):
    __doc__ = u'''yonghulingyang'''
    __tablename__ = 'yonghulingyang'


    __authTables__={'yonghuming':'yonghu'}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    lingyangbiaoti=models.CharField ( max_length=255,null=False,unique=False, verbose_name='领养标题' )
    chongwumingcheng=models.CharField ( max_length=255,null=True,unique=False, verbose_name='宠物名称' )
    fenlei=models.CharField ( max_length=255,null=True,unique=False, verbose_name='分类' )
    chongwuzhuangtai=models.CharField ( max_length=255,null=True,unique=False, verbose_name='宠物状态' )
    tupian=models.CharField ( max_length=255,null=True,unique=False, verbose_name='图片' )
    nianling=models.CharField ( max_length=255,null=True,unique=False, verbose_name='年龄' )
    lingyangfeiyong=models.CharField ( max_length=255,null=True,unique=False, verbose_name='领养费用' )
    shenqingneirong=models.TextField ( null=False, unique=False, verbose_name='申请内容' )
    shenqingriqi=models.DateField ( null=True, unique=False, verbose_name='申请日期' )
    shenqingbeizhu=models.CharField ( max_length=255,null=True,unique=False, verbose_name='申请备注' )
    yonghuming=models.CharField ( max_length=255,null=True,unique=False, verbose_name='用户名' )
    shouji=models.CharField ( max_length=255,null=True,unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255,null=True,unique=False, verbose_name='是否审核' )
    shhf=models.TextField ( null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255,null=True,unique=False, verbose_name='是否支付' )
    '''
    lingyangbiaoti=VARCHAR
    chongwumingcheng=VARCHAR
    fenlei=VARCHAR
    chongwuzhuangtai=VARCHAR
    tupian=VARCHAR
    nianling=VARCHAR
    lingyangfeiyong=VARCHAR
    shenqingneirong=Text
    shenqingriqi=Date
    shenqingbeizhu=VARCHAR
    yonghuming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'yonghulingyang'
        verbose_name = verbose_name_plural = '用户领养'

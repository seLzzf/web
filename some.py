#自动登录
验证:authenticated_user=authenticate(username=user.username,password=request.POST['password'])
登录:login(request,authenticated_user)
#两个密码框
try:
	ps1=user_form.cleaned_data['password1']
except:
	ps2=user_form.cleaned_data['Password2']
#？？？？？
user.set_password(user.password)
#获取表单信息的两种方式
email=request.POST.get('email')
email=user_form.cleaned_data['email']
#实例化form,若request中没有信息，则默认使用instance中的信息
form=UserProfileForm(request.POST,request.FILES,instance=userinfo)
form=UserProfileForm(request.POST,userinfo)
#有关get和filter的用法知识点，|将两个查询集合并
the_follower=Follower.objects.get(owner=page_user,follower=user)
message1=Message.objects.filter(t_m=T_M,私密留言=False)
message2=Message.objects.filter(t_m=T_M,私密留言=True,giver=request_user)
messages=message1|message2
#pic储存为用户名
if pic:
	pic_last=str(pic).split('.')[-1]
	pic_name='images/'+str(user.id)+'.'+pic_last
	pic=Image.open(pic)
	pic.save('media/'+pic_name)
userinfo.save()
#关于用户表单
UserCreationForm中自带两个密码框
#session相关
request.session['x']='y'
request.session.get('x')
#基于类...
def get_queryset(self):
    cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#显示用户上传图片
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from news.models import *
u1 = User.objects.create_user(username= 'User1')
u2 = User.objects.create_user(username= 'SecondUser2')
Author.objects.create(authorUser = u1)
Author.objects.create(authorUser = u2)
Category.objects.create(name = 'FirstCategory')
Category.objects.create(name = 'SecondCategory')
Category.objects.create(name = 'thirdCategory')
Category.objects.create(name = 'fourthCategory')
a1 = Author.objects.get(id=1)
a2 = Author.objects.get(id=2)

Post.objects.create(author = a1, categoryType = 'NW', title = 'Титульник Автора а1 категория NW', text='большой текст')
Post.objects.create(author = a1, categoryType = 'AR', title = 'Титульник ддля AR1', text = 'big text for ar1')
Post.objects.create(author = a2, categoryType = 'AR',title = 'Титульник ддля AR2', text = 'big text for ar2')

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))


Comment.objects.create(commentPost=Post.objects.get(id=1),commentUser=Author.objects.get(id=1).authorUser,text='текст комментария первого автора к 1ому посту')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=2).authorUser,text='текст комментария2')
Comment.objects.create(commentPost=Post.objects.get(id=3),commentUser=Author.objects.get(id=2).authorUser,text='текст комментария3')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=1).authorUser,text='текст комментария4')


Comment.objects.get(id=3).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()

x =Author.objects.get(id=1)
x2 =Author.objects.get(id=2)
x.update_rating()
x2.update_rating()

q = Author.objects.order_by('-ratingAuthor')
q[0].ratingAuthor
Post.objects.get(id=1).like()
#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
q2 = Post.objects.order_by('-rating')
(q2[0].dateCreation, q2[0].author.authorUser.username, q2[0].rating,q2[0].title, q2[0].preview())


q







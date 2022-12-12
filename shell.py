user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')


Author.objects.create(author=User.objects.get(id=1))
Author.objects.create(author=User.objects.get(id=2))

cat1 = Category.objects.create(category= 'Экономика')
cat2 = Category.objects.create(category= 'Политика')
cat3 = Category.objects.create(category= 'Армия')
cat4 = Category.objects.create(category= 'Наука')

papers1 = Post.objects.create(post_author=Author.objects.get(id=1), event_choose = 'PP',
                              title='"Укрэнерго" получило госгарантии на реконструкцию энергообъектов',
                              post_text='МОСКВА, 11 дек - РИА Новости. В национальной энергетической компании "Укрэнерго" сообщили, что правительство Украины предоставило госгарантии на проекты по восстановлению и реконструкции энергообъектов компании на общую сумму более 400 миллионов евро, эти средства будут направлены на приобретение необходимого оборудования.Отмечается, что в скором времени компания сможет приобрести часть критически необходимого оборудования для восстановления сетевой инфраструктуры.',
                              )

papers2 = Post.objects.create(event_choose = 'PP',
                              post_author = author1,
                              categories= cat1, cat3,
                              title='"Укрэнерго" получило госгарантии на реконструкцию энергообъектов',
                              post_text='МОСКВА, 11 дек - РИА Новости. В национальной энергетической компании "Укрэнерго" сообщили, что правительство Украины предоставило госгарантии на проекты по восстановлению и реконструкции энергообъектов компании на общую сумму более 400 миллионов евро, эти средства будут направлены на приобретение необходимого оборудования.Отмечается, что в скором времени компания сможет приобрести часть критически необходимого оборудования для восстановления сетевой инфраструктуры.',
                              )

news1 = Post.objects.create(event_choose = 'NS',
                              post_author = author2,
                              categories= cat2, cat1,
                              title='"Укрэнерго" получило госгарантии на реконструкцию энергообъектов',
                              post_text='МОСКВА, 11 дек - РИА Новости. В национальной энергетической компании "Укрэнерго" сообщили, что правительство Украины предоставило госгарантии на проекты по восстановлению и реконструкции энергообъектов компании на общую сумму более 400 миллионов евро, эти средства будут направлены на приобретение необходимого оборудования.Отмечается, что в скором времени компания сможет приобрести часть критически необходимого оборудования для восстановления сетевой инфраструктуры.',
                              )


Post.objects.get(id=1).categories.add(Category.objects.get(id=1))
Post.objects.get(id=1).categories.add(Category.objects.get(id=3))
Post.objects.get(id=1).categories.add(Category.objects.get(id=4))

Post.objects.get(id=2).categories.add(Category.objects.get(id=1))
Post.objects.get(id=2).categories.add(Category.objects.get(id=5))

Post.objects.get(id=3).categories.add(Category.objects.get(id=1))
Post.objects.get(id=3).categories.add(Category.objects.get(id=2))


Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=2).author_user,comment_text="Good!")
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=1).author_user,comment_text="Nice")
Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=Author.objects.get(id=1).author_user,comment_text="SUPER")
Comment.objects.create(comment_post=Post.objects.get(id=3),comment_user=Author.objects.get(id=2).author_user,comment_text="The best!!!")


Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()

Post.objects.get(id=2).dislike_post()
Post.objects.get(id=3).dislike_post()
Post.objects.get(id=3).dislike_post()
Post.objects.get(id=1).post_rating
Post.objects.get(id=2).post_rating
Post.objects.get(id=3).post_rating



Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=2).like_comment()
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=3).like_comment()
Comment.objects.get(id=3).like_comment()
Comment.objects.get(id=4).like_comment()
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=1).dislike_comment()
Comment.objects.get(id=2).dislike_comment()
Comment.objects.get(id=3).dislike_comment()
Comment.objects.get(id=1).comment_rating
Comment.objects.get(id=2).comment_rating
Comment.objects.get(id=3).comment_rating
Comment.objects.get(id=4).comment_rating




Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).author_rating

Author.objects.get(id=2).update_rating()
Author.objects.get(id=2).author_rating



Author.objects.all().order_by('-author_rating').values('author_user__username', 'author_rating')[0]


q=1
list10 = [Author.objects.get(id=q).author_user.date_joined,
          Author.objects.get(id=q).author_user.username,
          Author.objects.get(id=q).author_rating,
          Post.objects.filter(post_author = Author.objects.get(id=q)).order_by('-post_rating').first().title
          ]




Post.objects.all().order_by('-post_rating')[0].comment_set.values('time_in_comment', 'comment_user', 'comment_rating', 'comment_text')


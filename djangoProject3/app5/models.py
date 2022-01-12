from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)

    def __str__(self):
        return self.tel + ', ' + self.tel + ', ' + self.addr

class qna(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ', ' + self.content + ', ' + self.write
# models class 하나당 RDB의 테이블 하나로 맵핑
# class의 맴버변수 하나당 RDB테이블의 컬럼 하나로 맵핑
# Object Relational Mapping(ORM)
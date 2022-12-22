from .models import Page
import random

# 모든 데이터를 입력 받는다
# 입력받은 데이터를 하나씩 받는다.
# 범위에서 벗어난 데이터가 있다면
# 0~10 사이의 랜덤값을 부여한다
# 결과를 저장한다


def validate_pages():
    obejcts = Page.objects.all()
    for object in obejcts:
        if (0 > object.score) or (10 < object.score):
            print(object.id, "의 score가 유효성을 통과히지 못했습니다.")
            value = random.randint(0, 10)
            object.score = value
            object.save()

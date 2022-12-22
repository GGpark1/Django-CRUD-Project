from django.core.exceptions import ValidationError


def validate_no_hash(value):
    if '#' in value:
        raise ValidationError("제목과 내용에 '#'를 사용할 수 없습니다.")


def validate_no_numbers(value):
    for ch in value:
        if ch in map(lambda x: str(x), list(range(0, 9))):
            raise ValidationError("'감정 상태'에 숫자를 사용할 수 없습니다.")


def validation_score(value):
    if (value < 0) or (value > 10):
        raise ValidationError("'감정 점수'는 0부터 10사이의 숫자만 들어갈 수 있습니다.")

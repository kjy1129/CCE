import base64
import urllib.parse
from itertools import cycle
import json

# 1. URL 디코딩된 쿠키 문자열
raw_cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"
decoded_cookie = urllib.parse.unquote(raw_cookie)

# 2. base64 디코딩
cookie_bytes = base64.b64decode(decoded_cookie)

# 3. 예상 평문 (기본값)
plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'

# 4. XOR 키 추출
key = ''.join(chr(c ^ ord(p)) for c, p in zip(cookie_bytes, plaintext))

# 5. 새로 만들 평문 (비밀번호 보이게)
new_plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'

# 6. 평문을 XOR 암호화
new_encrypted = ''.join(
    chr(ord(c) ^ ord(k)) for c, k in zip(new_plaintext, cycle(key))
)

# 7. base64 인코딩
new_cookie = base64.b64encode(new_encrypted.encode()).decode()

# 8. 출력
print("[+] 추출된 XOR 키:", key)
print("[+] 수정된 쿠키 값:", new_cookie)

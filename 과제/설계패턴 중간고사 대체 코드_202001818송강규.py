from abc import ABC, abstractmethod

# Factory Pattern
class WebPageFactory:
    def create_web_page(self, type):
        # 웹 페이지 유형에 따라 객체를 생성하는 팩토리 메서드입니다.
        if type == 'PC':
            return PCWebPage()
        elif type == 'Responsive':
            return DecoratorWebPage(ResponsiveWebPage())
        elif type == 'Mobile':
            return ProxyWebPage(MobileWebPage())
        else:
            raise ValueError('Unknown Web Page Type')

# 기본 웹 페이지 인터페이스
class WebPage(ABC):
    @abstractmethod
    def display(self):
        # 모든 웹페이지는 display 메서드를 구현해야 합니다.
        pass

# 구체적인 웹 페이지 구현
class PCWebPage(WebPage):
    def display(self):
        print("Displaying PC WebPage")

class ResponsiveWebPage(WebPage):
    def display(self):
        print("Displaying Responsive WebPage")

class MobileWebPage(WebPage):
    def display(self):
        print("Displaying Mobile WebPage")

# Decorator Pattern
class DecoratorWebPage(WebPage):
    def __init__(self, web_page):
        self._web_page = web_page  # 다른 웹 페이지를 감싸는 데코레이터

    def display(self):
        # 데코레이션 이전의 원래 기능을 호출
        self._web_page.display()
        # 추가적인 기능 또는 스타일을 적용
        print("Decorated WebPage")

# Proxy Pattern
class ProxyWebPage(WebPage):
    def __init__(self, web_page):
        self._web_page = web_page  # 대리 실행할 웹 페이지

    def display(self):
        # 접근 제어 또는 사전 처리
        print("Proxy before access.")
        self._web_page.display()
        # 필요시 사후 처리를 수행

# 클라이언트 코드
factory = WebPageFactory()

web_page_type = ['PC', 'Responsive', 'Mobile']
for wt in web_page_type:
    web_page = factory.create_web_page(wt)
    print(f"--- {wt} WebPage ---")
    web_page.display()

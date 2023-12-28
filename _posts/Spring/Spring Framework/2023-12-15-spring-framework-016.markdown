---
layout: post
title:  "컨트롤러"
date:   2023-12-15 13:19:00 +0900
categories: Spring&nbsp;Framework
tags: [컨트롤러]
---

### 컨트롤러 어노테이션 (@Controller)

-  해당 클래스를 "Controller"로 등록하기 위해 사용하는 어노테이션
-  @Controller 어노테이션을 적용하면 해당 클래스가 bean으로 등록되며,  
해당 클래스가 Controller로 사용할것임을 프레임워크에 알린다.

### 컨트롤러의 역할

- 컨트롤러는 단순히 요청을 받아 해당 요청에 맞는 서비스에 데이터를 주입하는 역할을 한다.
- 서비스는 비즈니스 로직이기 때문에 단순한 자바 코드로만 이루어져야 하기 때문에  
HttpServletRequest나 HttpServletResponse와 같은 객체를 매개 변수로 받아서 처리하는 역할은 컨트롤러에서 해야 한다.

### 주소 매핑하기

- 주소 매핑 어노테이션 종류
    - @RequestMapping : RequestMethod를 지정해서 호출하는 방식
    - @GetMapping : RequestMethod를 GET으로 고정해서 호출하는 방식
    - @PostMapping : RequestMethod를 POST로 고정해서 호출하는 방식
- 어노테이션이 선언된 컨트롤러 클래스의 모든 메소드가 하나의 요청에 대한 처리를 할 경우에 사용한다.
- @RequestMapping 어노테이션에 대한 모든 매핑 정보는 스프링에서 제공하는 HandlerMapping 클래스가 가지고 있다.
- @RequestMapping의 value 속성에는 요청될 url을, method 속성에는 요청 방식에 대해 작성한다.
    {% highlight java %}
        @RequestMapping(value = "/blog/main", method = RequestMethod.GET)
        public String blogMain(Model model) throws Exception{ ... }
    {% endhighlight %}
- @RequestMapping을 적용한 메소드 사용 시 뷰 네임을 적용하는 방법
    - String : return에 명시한 문자열을 읽고 그 값에 해당하는 페이지를 찾아서 매칭시킨다.
    - void : return이 따로 없기 때문에 요청한 url 주소에 따라서 뷰를 매칭시킨다.
    - 이외에도 VO나 Map로도 전달할 수도 있다. (이 경우에도 요청 url 주소에 따라서 뷰 매칭)
    - Spring 5에서 지원해주는 reactive streams도 가능하다. (Mono, Flux)
- forward 방식과 redirect 방식
    - forward 방식
        - 요청 주소 : /test/A
        - return : return "/test/B";
        - URL : http://localhost:8083/test/A
        - 매칭되는 뷰 : B.jsp
    - redirect 방식
        - 요청 주소 : /test/C
        - return : return "redirect:/test/D";
        - URL : http://localhost:8083/test/D
        - 매칭되는 뷰 : D.jsp
- @GetMapping과 @PostMapping
    - @GetMapping("요청 주소")
        - @RequestMapping(value = "요청 주소", method = RequestMethod.GET)의 요약
    - @PostMapping("요청 주소")
        - @RequestMapping(value = "요청 주소", method = RequestMethod.POST)의 요약

### 값 전달하기/전달받기

- name 속성의 따른 값 (@RequestParam 어노테이션) : 명시한 name 속성명에 따라 전달받은 값을 골라서 받는다.
    - @RequestParam을 통해 전달받을 값을 String으로 지정했을 때, 만약 전달받은 값이 String이 아닐 경우 자동으로 형변환한다.
    - required 속성을 명시하면 필수 여부를 선택할수 있다. (기본 값 : true)
        - 예시 ) @RequestParam(value="nickname", required=false) String nickname
    - 필수 값이지만 값이 들어오지 않으면 오류가 발생하기 때문에 이를 위해 기본 값을 설정할수 있다.
        - 예시 ) @RequestParam(value="mode", defaultvalue="view") String mode
    - 기본 예시
        {% highlight java %}
        @RequestMapping(value="/find/account", method = RequestMethod.GET)
        public String findId(@RequestParam("name") String name, @RequestParam("birthday") String birthday) {
            System.out.pringln("계정 찾기 - 이름 : " + name + " / 생년월일 : " + birthday);
            //요청 url : http://localhost:8083/blog/proflie?name=홍길동&birthday=970229
            //출력 : 계정 찾기 - 이름 : 홍길동 / 생년월일 : 970229
            
            return "/find/account";
        }
        {% endhighlight %}
- 요청 url에 따른 동적 값 (@PathVariable 어노테이션) : @RequestMapping의 URL 값의 중괄호에 명시된 패스 변수를 받는다.
    - 기본 예시
        {% highlight java %}
        @RequestMapping(value="/blog/{id}", method = RequestMethod.GET)
        public String personalBlog(@PathVariable("id") String id) {
            System.out.pringln("방문 블로그 : " + id);
            //요청 url : http://localhost:8083/blog/helloworld
            //출력 : 방문 블로그 : helloworld

            return "/blog/personal";
        }
        {% endhighlight %}

### 비동기 통신

- @RestController 어노테이션
    - @Contrller 어노테이션 + @Response 어노테이션
- 주로 ajax같은 비동기 통신을 하여 데이터 처리를 하기 위해서는  
http 요청의 본문에 데이터를 담아하기 때문에  
@ResponseBody나  @RequestBody같은 어노테이션이 필요하다.
- 요청 본문 (@RequestBody)
    - http 요청의 바디내용을 통째로 자바객체로 변환해서 매핑된 메소드 파라미터로 전달해준다.
- 응답 본문 (@ResponseBody)
    - @ResponseBody 어노테이션이 붙은 컨트롤러는 요청을 받았을 때  
    해당 http 요청의 미디어타입과 파라미터의 타입을 먼저 확인한다.
    - return으로 전달하려는 자바 객체를 http 요청의 타입에 맞게  
    MessageConverter를 통해 변환하여 클라이언트로 전송한다.
- 비동기 통신 관련 컨트롤러 예시
{% highlight java %}
@ResponseBody
@RequestMapping(value = "/blog/main/ajax", method = RequestMethod.POST)
public Map<String, Object> blogMainPostAjax(@RequestBody HashMap<String, Object> map,  Model model) throws Exception {

    ...

    Map<String, Object> result = new HashMap<String, Object>();
    result.put("message", "success");

    return result;
}
{% endhighlight %}

### RequestMethod

- GET : 클라이언트에서 서버로 어떠한 리소스로 부터 정보를 요청하기 위해 사용되는 메서드
    - GET 요청은 캐시가 가능하다.
    - GET 요청은 브라우저 히스토리에 남는다.
    - GET 요청은 북마크 될 수 있다.
    - GET 요청은 길이 제한이 있다. (표준은 없지만 브라우저마다 제한이 다르다.)
    - GET 요청은 url에 파라미터가 모두 노출되기 때문에 중요한 정보를 다루면 안된다.
    - GET 요청은 데이터를 요청할 때만 사용 된다.
    - GET 요청은 url 파라미터에 요청하는 데이터를 담아 보내기 때문에 http 메시지에 body가 없다.
- POST : 클라이언트에서 서버로 리소스를 생성하거나 업데이트하기 위해 데이터를 보낼 때 사용 되는 메서드
    - POST 요청은 캐시되지 않는다.
    - POST 요청은 브라우저 히스토리에 남지 않는다.
    - POST 요청은 북마크 되지 않는다.
    - POST 요청은 데이터 길이에 제한이 없다.
    - POST 요청은 body 에 데이터를 담아 보내기 때문에 당연히 http 메시지에 body가 존재한다.

### View 페이지에 데이터 전달하기

● Model 객체
    - Controller에서 생성한 데이터를 담아서 View로 전달할 때 사용하는 HashMap의 형식의 객체
● Model 객체 사용법
    {% highlight java %}
    @RequestMapping(value = "/blog/{userID}", method = RequestMethod.GET)
    public String personalBlog(@PathVariable String userID, Model model) throws Exception {
        model.addAttribute("mode", "view"); //게시글 보기 모드
        return "/blog/personal";
    }
    {% endhighlight %}
● Model 객체를 파라미터로 사용하지 않고 특정 파라미터를 직접 view에 매칭시키는 방법
    {% highlight java %}
    @RequestMapping(value = "/blog/{userID}", method = RequestMethod.GET)
    public String personalBlog(@PathVariable String userID, @ModelAttribute("mode") String mode, Model model) throws Exception {
        //@ModelAttribute 어노테이션은 multipart/form-data 형태의 HTTP Body 내용과 HTTP 파라미터들을 1대1로 객체에 바인딩시킨다.
        //@ModelAttribute 어노테이션에 파라미터명을 명시하면 요청 url에 ModelAttribute로 명시된 값이 필요하다.
        //ModelAttribute("mode")처럼 정확하게 명시하지 않고 ModelAttribute User user처럼 사용할 수도 있다.
        //만약 Setter함수가 없다면 매핑을 시키지 못하고, null을 갖게 된다.

        return "/blog/personal";
    }
    {% endhighlight %}
● ModelAndView 객체 : Model과 View를 동시에 설정가능한 형식의 객체 (ModelAndView 객체를 리턴한다.)
    {% highlight java %}
    @RequestMapping(value = "/blog/{userID}", method = RequestMethod.GET)
    public ModelAndView personalBlog(@PathVariable String userID, Model model) throws Exception {
        ModelAndView mv = new ModelAndView();
        mv.setViewName("/blog/personal"); //뷰명
        mv.addObject("mode", "view"); //뷰로 보낼 데이터

        return mv;
    }
    {% endhighlight %}

### Rendering 인터페이스

- Spring 5부터 지원
- 기본 형식
    {% highlight java %}
    @매핑_어노테이션("요청 url")
    public Rendering 메소드명() {
        return Rendering
            .view("뷰명")
            .modelAttribute("모델명", 데이터)
            .build();
    }
    {% endhighlight %}
# ③ 正则表达式

**Q：什么是正则？**

> 所谓**正则表达式**，即：事先定义好一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤 

常见的正则表达式的方法有？

- re.compile: 编译
- pattern.math: 从头找一个
- pattern.search: 找一个
- pattern.findall: 找所有
- pattern.sub: 替换

![1644842783794](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644842783794.png)

说明：

- `.`的Dotall即模式即是在匹配时加上re.Dotall参数，或者re.S，使`.`能够匹配任意字符

- 记忆：d：digit；s：space

- sub的使用，re.sub(reg, new_str, old_str)，将匹配到的内容替换为new_str

- re.findall('a(.*)b', 'str')，能够返回括号中的内容，括号前后的内容起到定位和过滤的效果

- r'a\nb' 可以匹配'a\nb'；r'a\nb'而不能匹配'a\nb'，r可以忽略转义符号带来的影响，待匹配的字符串里面有 几个\，正则表达式里面也写几个\即可

- **compile的作用**

  - 将对应正则表达式能够匹配到的内容放到内存中去，加快匹配的速度
  - 使用方法：re.compile(reg)

- **compile和sub的结合使用**

  

  ```python
  b = hello1world2
  p = re.compile('\d')
  p.findall(b)
  p.sub('_',b)    #将b中的所有数字替换为下划线
  ```

  ps：如果是对`.`进行编译，若想使其能够匹配换行符等，则re.S需要加在编译的使用，而不是匹配的时候

**贪婪模式与非贪婪模式**

- 非贪婪模式：`.*?`或者`.+?` 
- 贪婪模式：`.*`或者`.+`
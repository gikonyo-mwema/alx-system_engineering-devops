0x06. Regular expression

Regex

DevOps

Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

## Tasks and resources

The links below cover every tracked task file and supporting resource in this project folder.

- [0-simply_match_school.rb](./0-simply_match_school.rb) — Source file for Simply match school.
- [1-repetition_token_0.rb](./1-repetition_token_0.rb) — Source file for Repetition token 0.
- [100-textme.rb](./100-textme.rb) — Source file for Textme.
- [2-repetition_token_1.rb](./2-repetition_token_1.rb) — Source file for Repetition token 1.
- [3-repetition_token_2.rb](./3-repetition_token_2.rb) — Source file for Repetition token 2.
- [4-repetition_token_3.rb](./4-repetition_token_3.rb) — Source file for Repetition token 3.
- [5-beginning_and_end.rb](./5-beginning_and_end.rb) — Source file for Beginning and end.
- [6-phone_number.rb](./6-phone_number.rb) — Source file for Phone number.
- [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb) — Source file for OMG WHY ARE YOU SHOUTING.

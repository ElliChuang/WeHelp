### 要求三
1. 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
   ```mysql
   insert into member(name,username,password)
   values('test','test','test');
   insert into member(name,username,password)
   values('Amy Wang','Amy','iamamy');
   insert into member(name,username,password)
   values('Claire Su','Claire','iamclaire');
   insert into member(name,username,password)
   values('Max Lin','Max','iammax');
   insert into member(name,username,password)
   values('Alen Chau','Alen','iamalen');
   insert into member(name,username,password)
   values('Ivy Chuang','Ivy','iamivy');
   insert into member(name,username,password)
   values('Ian Chu','Ian','iamian');
   ```
   ![3-1](https://user-images.githubusercontent.com/111445341/196464900-8de91c07-dd37-4f0f-bdb1-6daa3f972c0a.png)

2. 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
   ```mysql
   select * from member;
   ```
   ![3-2 ](https://user-images.githubusercontent.com/111445341/196473140-a0ef7ba9-1cf1-43ed-9916-f16f78199c53.png)

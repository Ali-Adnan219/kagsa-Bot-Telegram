# kagsa-Bot-Telegram

### community links community links library

[Telegram](https://t.me/kagsaBotTelegram)

### To install kagsa

```bash
pip install kagsa==1.1.0
```
### to run a bot

```bash
kagsa bot.kg
```
### Example

```bash
include "bots.kgl"
var token='5689364691:AAE-m5YBGMQ7QltUKxdS80JfFUNPjmOjVtE'



//send data
func PostDataBot(method,data){
    var sendmsg = bots.sendData(token,method,data)
    return sendmsg
}



func GetAllMsg(result){
var message=result.get("message")
var text= message.get("text")
var chat_id= message.get("chat")
var id=chat_id.get("id")

if text=="/start"{

var data=dict(chat_id=id,text="hi")
var method ="sendMessage"
PostDataBot(method,data)}

if text=="/help"{
var data=dict(chat_id=id,text="how l can help you")
var method ="sendMessage"
PostDataBot(method,data)}

//end func
}



while true {
var result =bots.polling(token)
if length(toStr(result)) > 8 {
GetAllMsg(result)}
//end while
}
```
 

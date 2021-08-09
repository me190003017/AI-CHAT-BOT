# AI-CHAT-BOT

This is a simple AI Chat Bot, build using rasa framework. Rasa provides flexible conversational AI for building text and voice-based assistants.

For Frontend we have used rasa’s standard frontend.

This chat bot give answer to any general questions related to IIT Indore. This can give answers to questions like about iiti, faculties/Professor, departments, placement, hostels, campus, events, medical facilities, sport facilities, international relations and many other questions.

These are simple steps to run this chat bot
- First create anaconda enviornment
- Open anaconda powershell 
     - type command `conda activate rasa`
     - type `rasa run -m models --enable-api --cors "*" --debug`
     - Or if you want to train model `rasa train`
     - then again type `rasa run -m models --enable-api --cors "*" --debug` and leave it 
- Open another anaconda powershell 
     - type command `conda activate rasa`
     - type `rasa run actions` and leave it
- Open another anaconda powershell 
     - type command `conda activate rasa`
     - type `python app.py`
     - then copy url on which it is running and paste in browser
     - and then ask our questions


<br/>
  
  <table margin="auto">
    <tr>
    <td><img src="https://imgshare.io/images/2021/08/08/IMG_20210808_181045.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-8.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-1.jpg" width=280 height=470></td>
    </tr>
   <tr>
    <td><img src="https://imgshare.io/images/2021/08/08/1-3.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-5.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-2.jpg" width=280 height=470></td>
    </tr>
   <tr>
    <td><img src="https://imgshare.io/images/2021/08/08/1-4.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-6.jpg" width=280 height=470></td>
    <td><img src="https://imgshare.io/images/2021/08/08/1-9.jpg" width=280 height=470></td>
    </tr>
   <tr>
    <td><img src="https://imgshare.io/images/2021/08/08/1-7.jpg" width=280 height=470></td>
   </tr>
 </table>
 
 


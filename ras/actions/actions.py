# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#!/usr/bin/env python
# coding: utf-8

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from .scraper import departments
from .scraper import faculty
from .scraper import alumni
from .scraper import about_iiti
from .scraper import fees_structure
from .scraper import research
from .scraper import infrastructure
from .scraper import contact
from .scraper import location
from .scraper import placements
from .scraper import international_relations
from .scraper import Events
from .scraper import News
from .scraper import admission
from .scraper import hostels
from .scraper import sports
from .scraper import medical

#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


class Action1(Action):
    def name(self) -> Text:
        return "action_department"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        departments=departments()
        ans="Here is list of all departments : \n"
        for a in departments:
            ans=ans+a+'\n'
        dispatcher.utter_message(text=ans)

        return []


class Action2(Action):
    def name(self) -> Text:
        return "action_faculty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        faculties=faculty()
        ans=""
        for a in faculties:
            ans=ans+a+'\n'
        dispatcher.utter_message(text=ans)

        return []


class Action3(Action):
    def name(self) -> Text:
        return "action_alumni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        alumni_dict=alumni()
        dispatcher.utter_message(text=str(alumni_dict))

        return []

class Action4(Action):
    def name(self) -> Text:
        return "action_about_iiti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=about_iiti()
       
        dispatcher.utter_message(text=ans)

        return []

class Action5(Action):
    def name(self) -> Text:
        return "action_fee_structure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=fees_structure()

        dispatcher.utter_message(text=ans)

        return []


class Action6(Action):
    def name(self) -> Text:
        return "action_research"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=research()

        dispatcher.utter_message(text=ans)

        return []



class Action7(Action):
    def name(self) -> Text:
        return "action_infrastructure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=infrastructure()

        dispatcher.utter_message(text=ans)

        return []


class Action8(Action):
    def name(self) -> Text:
        return "action_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=contact()
        
        dispatcher.utter_message(text=ans)

        return []

class Action9(Action):
    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ans=location()

        dispatcher.utter_message(text=ans)

        return []

class Action10(Action):
    def name(self) -> Text:
        return "action_placement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ans=placements()
        
        dispatcher.utter_message(text=ans)

        return []



class Action11(Action):
    def name(self) -> Text:
        return "action_international_relation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ans=international_relations()
        
        dispatcher.utter_message(text=ans)

        return []



class Action12(Action):
    def name(self) -> Text:
        return "action_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=Events()
       
        dispatcher.utter_message(text=ans)

        return []






class Action13(Action):
    def name(self) -> Text:
        return "action_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ans=News()
        
        dispatcher.utter_message(text=ans)

        return []



class Action14(Action):
    def name(self) -> Text:
        return "action_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ans=admission()
        
        dispatcher.utter_message(text=ans)

        return []



class Action15(Action):
    def name(self) -> Text:
        return "action_hostel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=hostels()
       
        dispatcher.utter_message(text=ans)

        return []


class Action16(Action):
    def name(self) -> Text:
        return "action_sport"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=sports()
       
        dispatcher.utter_message(text=ans)

        return []

class Action17(Action):
    def name(self) -> Text:
        return "action_medical"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ans=medical()
       
        dispatcher.utter_message(text=ans)

        return []
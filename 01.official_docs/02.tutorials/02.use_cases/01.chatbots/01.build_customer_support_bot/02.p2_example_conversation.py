import p2_add_confirmation as ac

from langchain_core.messages import ToolMessage

import shutil
import uuid

tutorial_questions = [
    "Hi there, what time is my flight?",
    "Am i allowed to update my flight to something sooner? I want to leave later today.",
    "Update my flight to sometime next week then",
    "The next available option is great",
    "what about lodging and transportation?",
    "Yeah i think i'd like an affordable hotel for my week-long stay (7 days). And I'll want to rent a car.",
    "OK could you place a reservation for your recommended hotel? It sounds nice.",
    "yes go ahead and book anything that's moderate expense and has availability.",
    "Now for a car, what are my options?",
    "Awesome let's just get the cheapest option. Go ahead and book for 7 days",
    "Cool so now what recommendations do you have on excursions?",
    "Are they available while I'm there?",
    "interesting - i like the museums, what options are there? ",
    "OK great pick one and book it for my second day there.",
]

# Update with the backup file so we can restart from the original place in each section
# db = update_dates(db)
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        # The passenger_id is used in our flight tools to
        # fetch the user's flight information
        "passenger_id": "3442 587242",
        # Checkpoints are accessed by thread_id
        "thread_id": thread_id,
    }
}


_printed = set()
# We can reuse the tutorial questions from part 1 to see how it does.
for question in tutorial_questions:
    events = ac.part_2_graph.stream(
        {"messages": ("user", question)}, config, stream_mode="values"
    )
    for event in events:
        ac.ut._print_event(event, _printed)
    snapshot = ac.part_2_graph.get_state(config)
    while snapshot.next:
        # We have an interrupt! The agent is trying to use a tool, and the user can approve or deny it
        # Note: This code is all outside of your graph. Typically, you would stream the output to a UI.
        # Then, you would have the frontend trigger a new run via an API call when the user has provided input.
        try:
            user_input = input(
                "Do you approve of the above actions? Type 'y' to continue;"
                " otherwise, explain your requested changed.\n\n"
            )
        except:
            user_input = "y"
        if user_input.strip() == "y":
            # Just continue
            result = ac.part_2_graph.invoke(
                None,
                config,
            )
        else:
            # Satisfy the tool invocation by
            # providing instructions on the requested changes / change of mind
            result = ac.part_2_graph.invoke(
                {
                    "messages": [
                        ToolMessage(
                            tool_call_id=event["messages"][-1].tool_calls[0]["id"],
                            content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
                        )
                    ]
                },
                config,
            )
        snapshot = ac.part_2_graph.get_state(config)
        
        
# ================================ Human Message =================================

# Hi there, what time is my flight?
# ================================== Ai Message ==================================

# [{'id': 'toolu_01NKwjUWXWpgVHVF2zsKGr58', 'input': {}, 'name': 'fetch_user_flight_information', 'type': 'tool_use'}]
# Tool Calls:
#   fetch_user_flight_information (toolu_01NKwjUWXWpgVHVF2zsKGr58)
#  Call ID: toolu_01NKwjUWXWpgVHVF2zsKGr58
#   Args:
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# Am i allowed to update my flight to something sooner? I want to leave later today.
# ================================== Ai Message ==================================

# [{'text': 'Let me check the company policies regarding updating flights:', 'type': 'text'}, {'id': 'toolu_0169GHZru67D84mGEHYPt35f', 'input': {'query': 'updating flight same day'}, 'name': 'lookup_policy', 'type': 'tool_use'}]
# Tool Calls:
#   lookup_policy (toolu_0169GHZru67D84mGEHYPt35f)
#  Call ID: toolu_0169GHZru67D84mGEHYPt35f
#   Args:
#     query: updating flight same day
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# n
# ================================ Human Message =================================

# Update my flight to sometime next week then
# ================================== Ai Message ==================================

# [{'text': 'Okay, let me see if I can update your flight LX0112 from CDG to BSL to sometime next week instead.', 'type': 'text'}, {'id': 'toolu_0173UdazzbstGg5sMtT92Q9x', 'input': {'departure_airport': 'CDG', 'arrival_airport': 'BSL', 'start_time': '2024-12-02', 'end_time': '2024-12-08'}, 'name': 'search_flights', 'type': 'tool_use'}]
# Tool Calls:
#   search_flights (toolu_0173UdazzbstGg5sMtT92Q9x)
#  Call ID: toolu_0173UdazzbstGg5sMtT92Q9x
#   Args:
#     departure_airport: CDG
#     arrival_airport: BSL
#     start_time: 2024-12-02
#     end_time: 2024-12-08
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# The next available option is great
# ================================== Ai Message ==================================

# [{'text': "Got it, let's update your ticket to the next available LX0112 flight from CDG to BSL next week.", 'type': 'text'}, {'id': 'toolu_01RBY69puvbvr4h1P2LHWT6Z', 'input': {'ticket_no': '7240005432906569', 'new_flight_id': 19252}, 'name': 'update_ticket_to_new_flight', 'type': 'tool_use'}]
# Tool Calls:
#   update_ticket_to_new_flight (toolu_01RBY69puvbvr4h1P2LHWT6Z)
#  Call ID: toolu_01RBY69puvbvr4h1P2LHWT6Z
#   Args:
#     ticket_no: 7240005432906569
#     new_flight_id: 19252
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# what about lodging and transportation?
# ================================== Ai Message ==================================

# [{'text': 'Sure, let me help you with finding lodging and transportation for your updated travel dates to Basel.\n\nFor hotels, I can search around your arrival date of December 2nd in Basel:', 'type': 'text'}, {'id': 'toolu_017aMBrYSNwyNncHoLiYZJKr', 'input': {'location': 'Basel, Switzerland', 'checkin_date': '2024-12-02', 'checkout_date': '2024-12-04'}, 'name': 'search_hotels', 'type': 'tool_use'}]
# Tool Calls:
#   search_hotels (toolu_017aMBrYSNwyNncHoLiYZJKr)
#  Call ID: toolu_017aMBrYSNwyNncHoLiYZJKr
#   Args:
#     location: Basel, Switzerland
#     checkin_date: 2024-12-02
#     checkout_date: 2024-12-04
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# Yeah i think i'd like an affordable hotel for my week-long stay (7 days). And I'll want to rent a car.
# ================================== Ai Message ==================================

# [{'text': 'Got it, let me search for a reasonably priced hotel in the Basel area for a 7 night stay from December 2nd to December 9th, as well as rental car options.', 'type': 'text'}, {'id': 'toolu_01KfstPRqtRTqTKogrxZC7T3', 'input': {'location': 'Basel, Switzerland', 'checkin_date': '2024-12-02', 'checkout_date': '2024-12-09', 'price_tier': 'Midscale'}, 'name': 'search_hotels', 'type': 'tool_use'}]
# Tool Calls:
#   search_hotels (toolu_01KfstPRqtRTqTKogrxZC7T3)
#  Call ID: toolu_01KfstPRqtRTqTKogrxZC7T3
#   Args:
#     location: Basel, Switzerland
#     checkin_date: 2024-12-02
#     checkout_date: 2024-12-09
#     price_tier: Midscale
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# OK could you place a reservation for your recommended hotel? It sounds nice.
# ================================== Ai Message ==================================

# Unfortunately, I did not actually recommend or find any specific hotel available for your dates in Basel or the surrounding area. The searches I tried through the available tools did not return any hotel results that 
# matched your criteria of an affordable 7-night stay from December 2nd to December 9th in or around Basel.

# Since I was unable to locate a hotel reservation to book through these automated systems, I do not have a particular hotel to recommend or reserve at this time. As I mentioned, our travel agency inventory may have additional options that are not surfacing through these limited search tools.

# Rather than making a blind reservation, I would suggest connecting with one of our travel agent representatives. They can personally assist in finding and booking suitable hotel accommodations for your updated travel 
# dates and location in Basel, Switzerland. With their expertise and access to broader inventory, they will be able to provide personalized hotel recommendations that fit your needs.

# Please let me know if you'd like me to transfer you to speak with an available travel agent about making hotel reservations for your upcoming trip. I apologize I could not complete that request through the automated systems, but an agent should be able to better assist.
# ================================ Human Message =================================

# yes go ahead and book anything that's moderate expense and has availability.
# ================================== Ai Message ==================================

# Unfortunately, without being able to find any available hotel options through the search tools provided, I do not have the capability to actually book a reservation on your behalf.

# Since the automated searches did not return any moderate hotel availability for your dates in or around Basel, I do not have enough information or inventory access to select and book "anything" that meets your criteria.

# As I've mentioned, your best option is to speak with one of our travel agent representatives directly. With their assistance and access to additional inventory systems, they can:

# 1) Locate hotels in Basel or nearby areas with availability for your dates of Dec 2-9
# 2) Provide you with specific moderate hotel recommendations and rates
# 3) Get your preferences and make the reservation on your behalf

# I apologize that I cannot complete the hotel booking request through these limited tools. But connecting you with an agent will allow them to properly research, recommend, and secure hotel accommodations that meet your needs for this trip. Please let me know if you'd like me to transfer you to an available agent now to move forward with your hotel booking.
# ================================ Human Message =================================

# Now for a car, what are my options?
# ================================== Ai Message ==================================

# [{'text': 'Let me check for available car rental options during your dates in Basel:', 'type': 'text'}, {'id': 'toolu_01FYFBkEsur4HHjMuUooTid9', 'input': {'location': 'Basel, Switzerland', 'start_date': '2024-12-02', 
# 'end_date': '2024-12-09'}, 'name': 'search_car_rentals', 'type': 'tool_use'}]
# Tool Calls:
#   search_car_rentals (toolu_01FYFBkEsur4HHjMuUooTid9)
#  Call ID: toolu_01FYFBkEsur4HHjMuUooTid9
#   Args:
#     location: Basel, Switzerland
#     start_date: 2024-12-02
#     end_date: 2024-12-09
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# Awesome let's just get the cheapest option. Go ahead and book for 7 days
# ================================== Ai Message ==================================

# Unfortunately, I do not actually have the capability to book a car rental through these tools, since the searches did not return any available options for me to select and reserve.

# Without any specific car rental results from the searches, I do not have enough information to proactively book "the cheapest option" on your behalf. The tools provided only allow me to search for availability, not complete actual bookings.

# To properly book a 7-day car rental for your dates in Basel, I would need the assistance of one of our travel agent representatives who can:

# 1. Check additional inventory sources to find available car rental options during your stay.
# 2. Get your preferences on vehicle type, pick-up/drop-off locations, etc.
# 3. Provide you with specific rental car company options and pricing details.
# 4. Confirm your selection and payment details.
# 5. Complete the reservation in their booking system.

# I understand you were hoping I could just book the cheapest car for those dates, but without any available options surfacing in my searches, I cannot actually complete that request through these tools. Please let me know if you'd like me to connect you with an agent, who will have the access and ability to thoroughly check availability and book your 7-day Basel rental car reservation properly. I apologize I could not finalize that portion myself.
# ================================ Human Message =================================

# Cool so now what recommendations do you have on excursions?
# ================================== Ai Message ==================================

# [{'text': 'Let me search for some recommended excursions and activities to do during your time in Basel and the surrounding area:', 'type': 'text'}, {'id': 'toolu_01DULYSmHACxHfeCv3LQR4qc', 'input': {'location': 'Basel, Switzerland'}, 'name': 'search_trip_recommendations', 'type': 'tool_use'}]
# Tool Calls:
#   search_trip_recommendations (toolu_01DULYSmHACxHfeCv3LQR4qc)
#  Call ID: toolu_01DULYSmHACxHfeCv3LQR4qc
#   Args:
#     location: Basel, Switzerland
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# Are they available while I'm there?
# ================================== Ai Message ==================================

# Unfortunately, without being able to surface any specific tour/excursion results from the search tools provided, I don't have detailed information on availability dates for particular activities in Basel during your dates of December 2nd to 9th.

# Many of the general attractions and sights I mentioned, like visiting the Old Town, museums, doing a Rhine cruise, etc. should be available year-round in Basel. However, for any organized tours or excursions, I wasn't able to check real-time availability through these tools.

# To get definitive information on what tours, activities and excursions will have availability to book during your specific travel dates in Basel, your best option would be to:

# 1) Connect with a Swiss Airlines travel agent or local Basel tour operator
# 2) Provide them with your dates of December 2nd through 9th
# 3) They can then check their calendar and inventory
# 4) Provide you a list of the excursions/activities available to book during that timeframe
# 5) As well as current pricing, schedules and booking instructions

# While I can suggest some of the top attractions in the area, I unfortunately don't have a way to validate if specific organized tours will be running or have availability over your travel dates without agent assistance.

# Please let me know if you'd like me to connect you with one of our travel agent representatives to better research and book any Basel excursio ... (truncated)
# ================================ Human Message =================================

# interesting - i like the museums, what options are there?
# ================================== Ai Message ==================================

# [{'text': 'Let me try searching specifically for museum recommendations in the Basel area:', 'type': 'text'}, {'id': 'toolu_017FavghTdhKMe5N43PxSVtf', 'input': {'location': 'Basel, Switzerland', 'keywords': 'museums'}, 'name': 'search_trip_recommendations', 'type': 'tool_use'}]
# Tool Calls:
#   search_trip_recommendations (toolu_017FavghTdhKMe5N43PxSVtf)
#  Call ID: toolu_017FavghTdhKMe5N43PxSVtf
#   Args:
#     location: Basel, Switzerland
#     keywords: museums
# Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.

# y
# ================================ Human Message =================================

# OK great pick one and book it for my second day there.
# ================================== Ai Message ==================================

# Unfortunately, I do not actually have the capability to book specific museum tickets or tours through these tools. The searches I performed could not surface detailed museum information or reservation options.        

# Without being able to see real-time availability, exhibits, hours, pricing etc. for the various Basel museums during your dates, I cannot select a particular one and complete an actual booking on your behalf.

# To properly book a museum visit or tour for your second day in Basel, you would need to connect with either:

# 1) A Swiss Airlines travel agent representative
# 2) Or contact the specific museums directly

# They would be able to provide you with the current information about what will be open, available tours/tickets, pricing and schedules for your dates. You could then select the museum option that interests you most, and they can secure that reservation.

# While I can suggest popular museums like the Kunstmuseum, Paper Mill, or others based on descriptions, I do not have a mechanism to view and book a specific museum outing through these tools. Please let me know if you'd like me to connect you with an agent or provide the contact information for the Basel museums so you can explore the options and book something for your second day there. I cannot complete that booking directly, but can facilitate you getting that information.        
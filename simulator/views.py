from django.shortcuts import render
import json

def simulator_view(request):
    # Define the scenarios as a list of dictionaries
    scenarios = [
        {
            "scenario": "You're at a nail salon, and you notice one of the workers seems extremely nervous and avoids eye contact. She flinches whenever the manager raises their voice and appears to be wearing clothes that don't fit her properly.",
            "choices": [
                "Leave after your appointment and assume it's none of your business.",
                "Speak to the worker and ask if they need help.",
                "Contact local authorities or a trafficking hotline."
            ],
            "feedback": [
                "This choice overlooks possible signs of trafficking. Ignoring the situation allows potential abuse to continue.",
                "While well-intentioned, this could escalate danger for the worker.",
                "The correct choice. Reporting discreetly ensures professionals handle the situation safely without endangering the worker or yourself."
            ],
            "teachingPoint": "Workers in trafficking situations often show fear, signs of control, or wear inappropriate clothing. The best course of action is to discreetly report your concerns to a trafficking hotline or authorities."
        },
        {
            "scenario": "At a hotel, you notice a teenage girl with an older man. She appears withdrawn, doesn't make eye contact, and clutches her phone like it's her lifeline. The man does all the talking when checking in, and the girl doesn't carry any luggage.",
            "choices": [
                "Ignore the situation because it's not your business.",
                "Confront the man and demand answers.",
                "Report your observations to hotel staff and suggest they call authorities."
            ],
            "feedback": [
                "Ignoring the signs of trafficking allows the abuse to continue. You could miss an opportunity to save a life.",
                "Confrontation is risky and could put the victim in more danger.",
                "The correct choice. Hotel staff are trained to handle such situations discreetly and involve the authorities when needed."
            ],
            "teachingPoint": "Hotels can be hotspots for trafficking. Noticing these behaviors and reporting them discreetly to staff or authorities can save someone's life. Never confront the suspected trafficker directly."
        },
        {
            "scenario": "You're shopping in a local market, and you see a young boy working behind a stall. He looks extremely tired, and when you ask him a question, he glances nervously at an adult nearby before answering.",
            "choices": [
                "Assume he's just helping his family and continue shopping.",
                "Report your concerns to authorities or a trafficking hotline.",
                "Try to rescue the child yourself."
            ],
            "feedback": [
                "This choice dismisses key signs of child labor trafficking, such as nervous behavior and signs of exhaustion. Always investigate further.",
                "The correct choice. Reporting ensures that trained professionals can assess the situation and intervene if necessary.",
                "Direct intervention could escalate the situation, endangering you and the child. Always rely on authorities to act."
            ],
            "teachingPoint": "Child labor is often a sign of trafficking. It's important to report your suspicions to authorities rather than intervening personally, as this could put the child at greater risk."
        },
        {
            "scenario": "You're on a train, and a young woman next to you appears to have bruises on her arms. She's accompanied by a man who speaks for her and becomes angry if she tries to answer anyone's questions. She looks terrified.",
            "choices": [
                "Ignore the situation because you don't want to cause a scene.",
                "Try to quietly get her alone and ask if she needs help.",
                "Call the police or a trafficking hotline and provide a description of the pair."
            ],
            "feedback": [
                "Ignoring signs of trafficking misses an opportunity to help a potential victim. Always trust your instincts and report concerns.",
                "While your intention is good, this could alert the trafficker and put the victim at greater risk. Avoid direct confrontation.",
                "The correct choice. Discreetly reporting to authorities ensures the victim's safety and allows proper investigation."
            ],
            "teachingPoint": "Traffickers often control their victims through fear and intimidation. Observing these signs and discreetly reporting to authorities can lead to intervention without escalating danger."
        },
        {
            "scenario": "While driving past a farm, you notice a group of workers who look exhausted, wearing inappropriate clothing for the weather, and living in makeshift tents nearby. You also see no signs of proper facilities or accommodations for them.",
            "choices": [
                "Assume they're just working hard and continue on your way.",
                "Stop and talk to them about their working conditions.",
                "Report your concerns to a trafficking hotline or labor rights organization."
            ],
            "feedback": [
                "Ignoring clear signs of forced labor perpetuates exploitation. Take action if you suspect trafficking.",
                "Speaking directly could alert traffickers and put the workers in danger. Traffickers often monitor victims closely.",
                "The correct choice. Reporting ensures the situation is investigated by authorities or labor organizations trained to handle trafficking cases."
            ],
            "teachingPoint": "Forced labor in agriculture is a common form of trafficking. Recognizing poor conditions and reporting them to the proper authorities or organizations is vital."
        }
    ]

    # Serialize the scenarios as JSON and pass to the template
    return render(request, 'simulator/simulator.html', {
        "scenarios": json.dumps(scenarios)  # Ensure valid JSON for the template
    })

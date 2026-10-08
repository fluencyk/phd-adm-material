Ver 1.26.85 

Sep 2025 

# **"DouFunDriving"** 

# **Toward a Co-Pilot Interaction Framework for Intelligent Vehicles** A System-Level Approach to Co-Driving Interaction and Collaborative HMI Modeling 

_Prof. Feng Lin - linfeng@dhu.edu.cn_ - _Donghua University Yujun Kong - ykong3@stevens.edu_ - _Stevens Institute of Technology_ 

### **Abstract** 

Many recent intelligent-vehicle systems are shifting toward a cabin arrangement in which driving control, environmental awareness, and task-oriented actions are shared among the driver, the passenger, and an automated subsystem that operates alongside them. Large continuous displays have become routine in these interiors, yet the interfaces placed on top of them often feel loosely connected and still oriented toward the driver. This design choice creates a direct constraint on how decision-making can be shared inside the cabin. As a result, the passenger is left with a somewhat partial co-pilot role—able to participate in navigation, situational checking, or selected in-car activities, but seldom steadily or coherently. 

This paper introduces DouFunDriving, a Dual Fun and Functional co-pilot driving framework intended to bring a more structured form of interaction between human occupants and the vehicle’s intelligence. The framework is composed of three parts: a task-and-permission model that clarifies how responsibilities shift across roles; an interaction grammar that shapes how proposals, confirmations, and related cues travel between parties; and a zoning scheme that ties these patterns to the spatial logic of the through-screen. To keep the framework practical, a lightweight prototyping path is also outlined, consisting of a front-end interaction layout, a back-end data-flow pipeline, and a scriptdriven logic layer powered by RAIDScript to express interaction rules in a compact and adjustable way. 

Two small scenario prototypes are used to illustrate how DouFunDriving can organize co-driving behavior in both navigation routines and third-space entertainment contexts. A short review plan is also included to support potential future empirical studies. The broader aim is to build a clearer and more system-grounded foundation for designing collaborative human–machine interfaces as intelligent vehicles move toward more autonomous and multi-actor modes of operation. 

**Keywords:** co-driving; intelligent vehicle HMI; driver–passenger collaboration; multi-actor interaction; through-screen interfaces; interaction grammar; prototyping frameworks 

## **1 Motivation** 

The electric-vehicle cabin is no longer a small experimenter cabin of the past five years, but now occupies mainstream computer space. The total sales of global plug-in EVs increased by slightly above 3 million units sold in 2020 to over seventeen million units sold in 2024, with the 2025 project having over twenty million units. Simultaneously, the smart modules serving the functions of perception, support, and connectivity have developed into a significant industry. ADAS revenues shifted between twenty and thirty billion at mid-2021 (at the pandemic recovery early turn point, as opposed to less than twenty billion at the beginning of the 

decade), and further growth is predicted in the remainder of the decade in the double-digit range. The same was the case with interaction-level automation: Level-2 co-pilot systems, which provide continuous steering and speed control, increased to almost one-fifth of U.S. new vehicles in model years 2021 to 2025. 

These changes combine to form opportunity and pressure. With the capabilities of hardware and software now enabling the integration of the cabin as a workspace between the driver, the passenger, and the AI, production HMIs have continued to reflect a single-driving logic with fractured displays and support features that render cooperation to im- 

Yujun Kong | Feng Lin 

provisation. The gap that motivates DouFunDriving is as follows: in case EV cabins are also turning into multi-actor computational environments, then an articulated co-pilot-based system of interaction is required to translate the capabilities into coherent, safe, enjoyable, and interesting shared-driving experiences. 

**Table 1** 

Global plug-in EV sales (million vehicles) 

|Years|2021|2023|2025(proj.)|
|---|---|---|---|
|Sales(M)|6.75|14.2|_>_20|



Data: EV-Volumes (2021, 2023) and IEA Global EV Outlook 2025 (projection). 

**Table 2** 

|Global ADAS market size(USD billions)||
|---|---|
|Years<br>2021<br>2023|2025|
|Revenue(bn)<br>23.4<br>34.0|37.1|



Data: Strategic Market Research (2021), Virtue Market Research (2023), Research Nester (2025). 

**Table 3** 

|Level-2 co-pilot systempenetration in U.S. new vehicles(%)|
|---|
|Years<br>2021<br>2023<br>2025*|
|Penetration(%)<br>7.5<br>21.9<br>—|
|Data: MITRE PARTS (2021, 2023). Values for 2025 pending<br>official release.|



The combination of these three trends is the same way, that is, electric cars are becoming more massive, the intelligent modules within them are becoming more stable, and the co-pilot-style assistance is not a fringe benefit anymore. The hardware supporting shared operation is already present in the cabin, but the interaction logic has lagged. Through this disjunction, it is the gap, which is that drives the more articulate, co-pilot-oriented grid–that grid capable of converting these increasing capabilities into a more articulated and reliable form of joint driving. 

## **2 Introduction** 

Often, modern intelligent-vehicle systems are designed to make the space inside the car more of a communal interaction zone than a control station as used by the driver. Tasks like motion control, environmental perception, and various activities that are task-oriented are nowadays usually shared between the driver, the passenger, and an automated 

subsystem that collaborates with the two. With increased automation capability, these functions become increasingly overlapping, so that the traditional single-driver interface looks constricted and inconvenient for the real usage of the cabin. Although broad, continuous displays take up the entire dashboard, the layers of interaction mounted on the displays are usually discontinuous and still point in the direction of the driver. 

Such an incongruity generates some conspicuous tension in decision-making within the cabin. Hardware is leading one to believe that there can be much more collaborative work going on in the space, yet the software often assumes that one individual is responsible for doing most of the situational reasoning. The passengers can sometimes assist in routing, check surrounding conditions, or control entertainment and other activities in the car, but still, they are usually not consistently involved and are characterized more by improvisation than by a structured design. With automated features having an increased role in operation, the lack of a clear co-driving logic causes the human and onboard system to not operate in a steady and synchronized way. 

Human-machine interface studies have covered visual interfaces, gesture systems, and other driverassistance systems; however, the overall architecture of linking the driver, the passenger, and the AI and HMI is loosely defined. There is minimal literature on the movement of a suggestion across roles, confirmation surface, and an event passing within the cabin. Similarly, the data streams that such collaboration needs are seldom specified in a manner that is directly prototyped or even subject to system-level analysis, and co-driving design has no consistent technical basis. 

This gap is covered in this paper. Our solution is DouFunDriving, a Dual Fun and Functional copilot system that is a coordinated interaction model within an intelligent cabin. The fun element replicates the experiential elements of sharing the driving, whereas the functional element imposes the structural discipline that is required to maintain collaboration both safe and repeatable. In order to measure this concept, we use the total co-driving experience as a weighted average of all the role contributions to the fun experience and to the functional performance on shared cabin tasks. Where r N d, p, a are the driver, passenger, and automated 

2 

Yujun Kong | Feng Lin 

subsystems; where t T is the tasks which include navigation, monitoring, or third-space. In the case of every role-task pair, we specify a fun-oriented contribution m fun r t and a functional contribution m func r t (weighted by their weighting factors w fun r t and w func r t, respectively). The overall cabin experience can be stated as below. 



Conventional driver-based HMIs put a lot of control and decision-making in the hands of the driver and minimal activities in the hands of the passenger. DouFunDriving re-balances this trend and involves the passenger as an active co-pilot and the AI with the same scope of responsibilities, instead of an assistant far away. According to this perspective, the framework not only brings new structures of interaction but also redistributes weighted contributions to roles in such a way that the fun and functional aspects of co-driving can be enhanced through safe conditions. Its essence consists of three components, namely a task-and-permission structure that renders responsibility transitions visible, an interaction grammar whereby the proposals and confirmations go round between the actors, and a zoning system that attaches these circulations to spatial areas on the screen. This structure is implemented in practice by a lightweight prototype path that comprises a front-end description of interaction, a back-end data flow pipeline, and a logic layer written in RAIDScript, in which interaction rules can be written in a small and testable form. 

This introduction is intended to clarify why the ever-increasing multi-actor nature of the cabin needs a better base in terms of a system-level approach. With the development of intelligent vehicles that become more autonomous in their behavior and distributed ways of operating, it becomes clearer that the driver, the passenger, and the AI should be considered as integrated components, but not separated. The first attempt to offer such a foundation is presented by DouFunDriving, which is conceptually framed and aligned with mechanisms that can be translated into real-world prototyping and designing practice. 

## **3 Related Work** 

The most recent research on automated-driving HMIs has primarily focused on ensuring that the driver is informed, engaged, and ready to resume control when necessary. Mehrotra et al. provide a general survey of automation interfaces used in vehicles and describe the design implications of feedback timing, modality selection, and safety signaling, showing that interface choices strongly shape driver understanding and intervention behavior (Mehrotra et al., 2021). Their work frames HMI as a safety channel through which system state and authority limits are communicated, but the driver remains the central operator, with passengers treated as secondary occupants. 

A second strand of research directs attention toward passengers and co-occupants of automated vehicles. Hartwich et al. examine passenger experience and trust, demonstrating that user-adaptive HMIs can significantly improve comfort and acceptance, although more information is not always beneficial across all user groups ( **?** ). Large et al. extend this by studying cooperative behavior between drivers and passengers in conditional automation, showing that passenger participation can redistribute workload, situational awareness, and safety-relevant behavior (Large et al., 2019). Both lines of work recognize the cabin as a multi-party social environment„ but do not develop a structured co-pilot model in which the passenger has explicit role definitions, task rights, and interaction modes. 

On the systems side, Feierle et al. present a multivehicle simulation in which an automated vehicle interacts with its passenger and an oncoming human driver at an urban bottleneck through synchronized internal and external HMIs (Feierle et al., 2020). Their model illustrates scenario-level communication but does not specify how responsibility, proposals, or confirmations circulate among the driver, passenger, and automation inside the cabin. More abstractly, Peintner et al. provide a taxonomy of human–vehicle cooperation, combining use cases, cooperation frames, and HMI components, and argue that automated-vehicle cooperation must be framed more holistically (Peintner et al., 2022). However, the taxonomy is descriptive and lacks a formal interaction grammar or task–permission structure connecting the driver–passenger–AI triad. 

DouFunDriving extends beyond these strands by 

3 

Yujun Kong | Feng Lin 

explicitly defining the cabin as a shared operational workspace and introducing a co-pilot–oriented interaction structure with task roles, permissions, interaction grammar, and spatial zoning. These components aim to provide a more systematic and prototypable foundation for collaborative HMI design in intelligent vehicles. 

## **4 Framework Overview** 

The interaction structure presented as DouFunDriving involves the driver, the passenger, and the AI system as coordinated agents, not independent agents. The framework is aimed at providing a system-level foundation of collaborative operation within an intelligent vehicle cabin, in which propositions, confirmations, and obligations must be regularly exchanged in a unified manner. Rather than depending on spontaneous gestures or disjointed interface indicators, DouFunDriving determines the manner in which tasks are passed on, how interaction flows between the three actors move in space, and how the flows are anchored to the throughscreen spatial logic. The framework is structured in three parts: task-permission structure, interaction grammar, and spatial zoning, which are supposed to provide the emerging multi-actor character of contemporary cabins with a more analyzable, stable, and implementable form of co-driving. 

### **4.1 Task–Permission** 

The task-permission structure is the model of the distribution of the driving and cabin functions between the driver, the passenger, and the AI system. Every actor has a task assigned with corresponding rights detailing who is permitted to initiate, approve, or cancel an action. The structure serves as a mere state model: an actor is either active, supportive, or observational, depending on the situation, and the changes in the state are only possible in case of predefined conditions. 

This is done by making these role transitions visible so as to allow all participants to view the existing distribution of responsibility. This eliminates ambiguous ownership and eliminates instances where the proposal/confirmation has been given without a responsible party. The structure eliminates the need to negotiate ad hoc to produce a co-driving behavior as well, and the structure provides a standard set of rules that the three participants move through in terms of activity and authority. 

### **4.2 Interaction Grammar** 

Interaction grammar stipulates the movement of the proposals, confirmations, and resolutions between the driver, the passenger, and the AI system. Every proposal is viewed as a structured unit of interaction in which its origin, the path of confirmation required, and the circumstances in which it can be accepted or rejected are recorded. Confirmations occur in a predetermined order in which one action cannot take place until the party making the confirmation has answered. Resolution is whereby the cabin promises a particular action and aligns the promise with all the participants. 

It is the grammar that is used as a minimal protocol to substitute the informal signaling with predictable patterns. It defines who can do what at what point, how to solve conflicting inputs, and what happens with a sequence that times out or is preempted. The grammar facilitates both analytical and direct implementation since it expresses interaction in terms of formal units and transitions, which enables the co-driving behavior within the cabin to develop in a predictable and experimental way. 

### **4.3 Spatial Zoning** 

The interaction grammar is related to the physical layout of the through-screen by the spatial zoning scheme. The cabin display is organized in proposal, confirmation, and status areas, with driver and passenger each being placed in such a way that there is no disruption with the other actors advancing towards a mutual action. The AI takes a central area where the system-generated suggestions and safety cues are shown in a manner that is seen by both human participants. 

The zoning has a role of interaction attached to it. The proposal zones focus on clarity and visibility, the confirmation zones assist in responding in a short and decisive manner, and the status zones give a continuous picture of the cabin state. The zoning scheme makes the logic of the framework grounded in an understandable visual scheme and minimizes ambiguity when the interaction units are shared with a clear division of the screen. This spatial anchoring is what makes the multi-actor workflow maintain its consistency even in situations where the participants are swapping their tasks rapidly. 

4 

Yujun Kong | Feng Lin 

## **5 Data Model and Logic Layer** 

**Data Model and Logic Layer** 12 13 The data model translates the co-driving interaction 14 into a sequence of structured events. Each event 1516 contains an actor tag, a role state, a task identifier,17 and a context bundle that reports driving conditions and cabin state. Actors may take the role of being active, supportive, or observational, and these states determine how the event is interpreted and what transitions are permissible in the system. Safety gates are also monitored to restrict actions that could influence vehicle control unless sufficient clarity and relevance are established. 12 3 To balance the contributions of the three actors, the 4 model uses a simple weighting function: 5 6 7 _W_ ( _a_ ) = _αRa_ + _βCa_ + _γSa,_ 89 where _Ra_ is the role state, _Ca_ is the clarity or 10 confidence of the input, and _Sa_ is its situational 1112 relevance. The coefficient values are tuned so 13 that safety-critical actions give more weight to the 14 15 driver and the AI, whereas experience-oriented activities give more weight to the passenger. This 16 weighting enables predictable arbitration when 17 multiple proposals occur in a short interval. 18 19 The logic layer processes the interaction grammar as an event-driven computation. Each proposal trig-20 gers a state transition, a confirmation request, or 21 a resolution step depending on both actor permis-22 sions and the current cabin state. Conflicts are re-23 solved by comparing weighted values of competing proposals; timeouts revert the cabin to the safest admissible alternative. The logic layer is implemented as a lightweight rule-book in RAIDScript, allowing interaction rules to be modified, tested, or extended without altering the system architecture. 

### **JSON Representation of an Event.** 

1 The following structure illustrates how a passenger2 generated routing proposal is encoded in the data 3 model: 4 ~~�~~ �5 1 { 6 2 "actor": "passenger", 7 3 "role_state": "supportive", 8 4 "task_id": "route_proposal", 9 5 "context": { 10 6 "speed": 38, 7 "visibility": "clear", 11 8 "traffic_level": "high", 9 "relevance": 0.82, 12 10 "clarity": 0.91 13 11 }, 14 

"payload": { 

- "proposal": "reroute_to_park", 

- "reason": "traffic_ahead" 

}, 

- "safety_gate": true 

} 

~~�~~ � 

### **Python Runtime Logic.** 

The system then evaluates the event through a small runtime function that computes the weight and issues a decision: 

~~�~~ � **def** evaluate_event(event, weights): ctx = event["context"] 

role = event["role_state"] clarity = ctx.get("clarity", 1.0) relevance = ctx.get("relevance", 1.0) W = ( weights["alpha"] * role_value(role) + weights["beta"] * clarity + weights["gamma"] * relevance ) 

**if** event["safety_gate"] **and** W < 0.55: **return** {"decision": "reject", " weight": W} **if** event["task_id"] == " route_proposal": **if** W >= 0.75: **return** {"decision": "confirm", "weight": W} **else** : **return** {"decision": "hold", " weight": W} **return** {"decision": "resolve", " weight": W} 

~~�~~ � 

### **Declarative RAIDScript Rule.** 

The same logic can be expressed compactly in RAIDScript, which serves as the logic layer for prototyping and modification: 

~~�~~ � < **interaction** task="route_proposal" actor="passenger"> < **context** speed="38" visibility="clear" traffic="high" relevance="0.82" clarity="0.91" /> 

< **weight** alpha="0.6" beta="0.25" gamma="0.15"> Compute W(a) = alpha*R + beta*C + gamma*S </ **weight** > 

< **logic** > 

5 

Yujun Kong | Feng Lin 

15 If safety_gate = true AND W(a) < 0 .55 --> reject 16 If W(a) >= 0.75 --> confirm 17 Else --> hold 18 On timeout --> resolve_safest 19 </ **logic** > 20 </ **interaction** > ~~�~~ � 

## **6 Prototype Implementation** 

The implementational prototyping is developed in the form of a small three-layer chain that reveals how the task-permission logic, interaction grammar, and spatial zoning can be integrated within an intelligent cabin, but not to aim at modeling the driving behavior, and whether the co-driving model can bear out in the form of data, rules, and visible interaction. 

- The front-end layer molds the through-screen surface to proposal, confirmation, and status regions, allocated to the driver, the passenger, and the AI. Every region has a limited number of structured components, including routing prompts, monitoring requests, acknowledgments, and cabin-state indicators. The design of the layout allows the three actors to play in parallel and without being blocked, and the AI occupies a small central zone where cues and safety messages generated by the system are always in sight. 

- The data-flow layer serves as the processing medium layer. It calculates the score of the event using the weighting function introduced above, transforms each interaction into a structured event, and normalizes the situation attributes. It is also in charge of the queue of unfinished events, validates the safety gates, enforces time-out rules, as well as arbitrates where multiple proposals look near in time. The idea is to allow the logic to be followed by data as opposed to the application of adhoc interface heuristics. 

- The interaction grammar is executed by the logic layer using a limited number of rules. Every proposal causes a rule block, which determines the necessity of the confirmation or the possibility of a change of role state, or the necessity of a direct resolution of the action by the cabin. The rules are coded in RAIDScript in order to keep them brief, declarative, and adaptable to the changes in the prototype. The layer demonstrates that the interaction gram- 

mar may be defined in the form of a concise manual that does not rely on imperative flow control. 

The three layers together constitute a bare minimum of an execution path. It illustrates that a multiactor cabin can be functioning in a predictable and verifiably reliable manner when the communication is pegged on fixed roles, fixed zoning, and rule-based course of actions. 

To supplement the three-layer prototype, there is the diagrammatic view, as shown below. 



**Figure 1** 

Three-layer prototype architecture of DouFunDriving. 

The former demonstrates the spatial design of the through-screen interface, indicating the positioning of the proposal, confirmation, and status areas to the driver, the passenger, and the AI. 

The second gives a more advanced workflow setup with the flow starting with the proposal formulation, and the resolution up to the cabinet level. 

These numbers do not represent production interface designs, but are structural references that are 

6 

Yujun Kong | Feng Lin 

associated with the data-flow and rule-based logic of the discussion above. 

## **7 Scenarios** 

The two short scenarios, as follows, depict how the suggested co-driving system works when the driver, the passenger, and the AI system engage in joint cabin activities. It is not aimed at the imitation of the driving process itself but demonstrates the functioning of the task-permission structure, interaction grammar, and spatial zoning as a chain. 

- The first situation relates to a modification of the scheduled path. The car is pursuing its timetable path, and the passenger observes that some impending social activity is about to cause a traffic jam. The routing proposal of the passenger is structured at the passenger region and transformed into an event with contextual features of relevance, clarity, and proximity to traffic. When the proposal has gone through the data-flow layer and has passed the safety gate, the event is signaled to the driver on the confirmation band. The logic layer interprets a recognition token through a brief acknowledgment by the driver. The event is then solved by the cabin and generates a common sphere of the navigation update that is visible to all three actors. The order is that an idea suggested by a passenger, however experience-based, can pass through an identical career of proposal, confirmation, and decision without undermining the supervisory role of the driver. 



**Figure 2** Scenario A: Passenger–AI Joint Route Proposal. 

- The second situation has to do with choosing a third-space activity. When the driving demand is low, a suggestion that has an enter- 

tainment nature is initiated by the passenger, including changing to a shared media mode. The event has a low safety weight value and a high experience weight value, and thus, the evaluator has a different way of processing it. The AI verifies the load that is being driven and identifies that the move can be made. An acknowledgment message is then sent to both the driver and the passenger and displayed in their areas. When the two actors are in supporting states, then the logic layer makes an automatic decision and switches the interface to the shared mode. Should there, however, be a change in the driving context before confirmation, the safety gate does not allow execution, and the system is reverted to the previous state. This situation demonstrates that an action based on experience can be negotiated in a controlled, reversible, and role-sensitive manner. 

Combining the two situations, it can be seen that the cabin is capable of supporting both functional choices, i.e., route changes, and experienceoriented activity planning based on the same structured chain of interaction. Another aspect that they emphasize is the bipolar nature of DouFunDriving, which provides the fun and functional elements of the cabin activity under the oversight of one integrated system of data, permissions, and interaction grammar. 

## **8 Limitation** 

DouFunDriving offers a systematic foundation for common operation within an intelligent cabin, but it restricts the degree to which it can be directly implemented in commercial automobiles. The current formulation simplifies numerous factors related to operations and has been practiced based on conceptual prototypes. These limitations denote the spaces in which more empirical and engineering activities are required to be done prior to the framework being regarded as strong. 

- The actual driving environment presents a series of external coupling variables, which are very dynamic-road safety variables, weather and lighting variations, network bandwidth variations, and even moment-to-moment driver-passenger interference. These are the factors that influence the formation of joint decisions, but the model that is currently in use 

7 

Yujun Kong | Feng Lin 

fails to describe them fully. Another significant limitation is integration: the current EV platforms are not similar in terms of timing guarantees, middleware stack, and proprietary control surface, and system-level integration cannot be consistently achieved. 

- Another weakness is related to the sporadic nature of manufacturer standards. There is a sharp difference between the vehicle display geometry, through-screen layout standards, HMI conventions, and data schema among automakers. In the context of such diversity, it is hard to transplant without alteration a co-driving model. Moreover, most UI/UX designers and in-vehicle software engineers are not exposed to a multi-actor role modeling or interaction grammar, which makes actual adoption in the real world slow. 

- There is yet another uncertainty associated with testing. Multi-actor interaction can reveal edge cases that unit, module, or system tests do not predict - particularly timing-related cases, arbitration bugs, and safety-fallback cases. Lastly, the discipline does not have a standardized process of gauging the quality of co-driving. The constructs of sharedcontrol fluency, clarity of roles, co-agency, and passenger experience have yet to obtain a consistent measure of evaluation. 

The limits will not suffice to underestimate the prospects of DouFunDriving, but they will indicate the scope of the current prototype and explain what kind of technical and empirical effort will be needed before it can be fully used at scale. 

## **9 Discussion** 

DouFunDriving conversation focuses on the ability to redesign the approach to the coordination of human and machine involvement through the structured co-driving model. The framework demonstrates that when activities, permissions, and communication patterns are codified, the multiactor cabin can leave improvised co-operation and progress towards a more frequent kind of shared operation. This brings the driver, the passenger, and the AI into a more definite relationship of functions, changes, and duties, rather than viewing them as individual actors. 

- One of the main issues that can be consid- 

ered as the result of this discussion is that codriving is not just a utilitarian process, but also an experience negotiation. The framework tries to strike a balance between the two by giving various weights to safety-critical and experience-oriented activities. This creates a more realistic image of the way co-operation occurs within an EV cabin: the driver still has oversight power; the AI ensures consistency and safety; and the passenger provides value but does not create a distraction. The interaction grammar and zoning scheme can offer a foundation of predictable behaviour, yet it is also indicative of how traditional drivercentric design can be brought to light. 

- The other observation is the behaviour of the system in the case of uncertainty. Due to the dynamics of the cabin environment, structured event processing and fallback policies assist in ensuring the stability of the environment when there is a timing or ambiguous input. This is made possible through the application of the weighted arbitration and safety gates that help the system to eliminate competing proposals without disrupting the hierarchy of roles. Simultaneously, the model emphasizes that rule-based interaction cannot work alone as future systems will require adaptive calibration mechanisms responding to circumstances, which create load and individual differences between users. 

- Lastly, the prototype will show that co-driving behaviour may be represented in a combination of data, layout logic, and rule execution, and not as a visual interface. This implies that a structured co-driving model could form the basis of a future intelligent-cabin system, assuming that it will be further expanded with detailed sensing, predictive logic, and empirical tuning. 

According to the discussion, DouFunDriving is therefore not a complete solution, but a preliminary system-level formulation that can be used to inform future research in human-vehicle collaboration. 

## **10 Future Work** 

The additional extension of DouFunDriving, of course, will be to go beyond a cabin-constrained model to a more flexible context-dependent model that can operate under different conditions of actual 

8 

Yujun Kong | Feng Lin 

driving. A number of directions are based on the work at hand. 

- To begin with, the co-driving regulations need to be empirically based. To note the reaction of drivers and passengers to negotiations over shared control, timing of confirmations, and cues based on zoning, both simulator-based and on-road controlled studies are required. This kind of study would assist in optimizing parameters in weighting, between role change, and arbitration behaviour in a way that cannot be provided by conceptual models. 

- Second, the rule-book governing the interaction can be reinforced with the help of adaptive mechanisms. Calibration based on learning can adapt the priorities in interactions during driving, a shift in the load or environmental complexity, or user behaviour. A more flexible system where a structured grammar is kept, but weighting is adjusted according to context, may provide a more believable kind of shared control that is predictable and yet more responsive to real-world circumstances. 

- Third, the prototype emphasizes that greater integration should be made with heterogeneous vehicle platforms. The next generation will involve formal interface layers that will connect the co-driving model to sensing systems, middleware, OEM control surfaces, and the external communication channels. A standardized task state schema, context bundle, and interaction event schema would facilitate cross-manufacturer and cross-cabin geometry deployment. 

- Fourth, better comprehensive assessment techniques are required. The existing evaluation of co-driving quality is somewhat fragmented, and such constructs as co-agency, sharedcontrol fluency, or passenger engagement lack developed measurement systems. The creation of these metrics is necessary to compare the results of the different co-driving models and ensure that there is improvement in the versions. 

We say, the current version of the DouFunDriving is cabin-driven by design. In a longer-term future, it can be developed as a more multi-actor, multisurface system, perhaps we can call it "MulFunDriving", where the cabin is no longer the central 

node in a distributed ambient-computing system. The mobile phone of the driver, the wearable devices of the passenger, and even the road infrastructure or city will add to the co-driving workflow in such an environment. This extension would entail new device zoning logic, additional rules on synchronization of proposals and confirmations, as well as modified safety-gate and arbitration mechanisms in cases where the environment itself has contextual information. This kind of development would shift the paradigm of in-cabin cooperation to a broader context of cooperative driving. 

## **11 Conclusion** 

Being an intelligently inspired, strictly developed framework towards the Next-Gen HCIMethodology-based Co-piloting research work on intelligent EVs, DouFunDriving provides a first system-level conceptualization of how drivers, passengers, and AI may interact as synchronized vehicles within an intelligent cabin. With the integration of task-permission logic, interaction grammar, and spatial zoning, the framework proves that multiactor co-driving can be formulated in a testable and predictable manner. The model is still a prototype, but it demonstrates that shared control can no longer be an improvised process, but rather a structured workflow that allows safety and experience to balance out. It is an initial move but provides an algorithmic foundation for the direction of future intelligent-cabin design and wider ambient and multi-surface cooperation in the next-generation cars. 

This work, "DouFunDriving", provides a preliminary system-level conceptualization of the manner in which drivers, passengers, and artificial intelligence may conduct themselves as integrated members within an intelligent cabin. The combination of task-permission logic, interaction grammar, and spatial zoning illustrates that multi-actor co-driving can be put in a predictable and testable form. Even though the model is a prototype, it demonstrates how the concept of shared control can go beyond the field of improvised cooperation to the level of a structured workflow that incorporates both safety and experience. 

Wholeheartedly, we evidenced that the academic support and guidance of the Visual Communication AGI Research Group and Lab of Donghua University, led by Prof. Feng Lin, and the support of the 

9 

Yujun Kong | Feng Lin 

XAI Lab through Prof. Zining Zhu with the NLPStars Hub of Stevens Institute of Technology have helped in this work. Their thoughts and debates have influenced the conceptual orientation and the methodological basis of this research. 

## **12 Reference** 

## **References** 

## **Contact** 

Email: 

ykong3@stevens.edu - Yujun Kong linfeng@dhu.edu.cn - Prof. Feng Lin Mobile: 

+1 201 736 2265 (U.S) 

[1] Mehrotra, A., Fishman, T., Ju, W., & Nass, C. (2021). A survey of human–automation interaction in automated driving interfaces. _Human Factors in Computing Systems_ . 

https://doi.org/10.1145/3411764 https://dl.acm.org/doi/10.1145/34117 64 

[2] Hartwich, F., Beggiato, M., & Krems, J. (2021). The influence of in-vehicle human–machine interfaces on passenger experience and trust in automated driving. _Transportation Research Part F: Traffic Psychology and Behaviour_ , 74, 162–177. 

https://doi.org/10.1016/j.trf.2020.0 8.019 

https://www.sciencedirect.com/scienc e/article/pii/S1369847820303573 

[3] Large, D., Burnett, G., Crundall, D., & Harvey, C. (2019). Driver–passenger coordination in conditional automated vehicles: The role of shared situational awareness. _Accident Analysis & Prevention_ , 132, 105266. https://doi.org/10.1016/j.aap.2019.1 05266 

https://www.sciencedirect.com/scienc e/article/pii/S0001457519304107 

[4] Feierle, A., Löcken, A., Bruder, R., & Baumann, M. (2020). Coordinated communication between automated vehicles and other road users: A multi-vehicle HMI simulation study. _Information_ , 11(10), 469. https://doi.org/10.3390/info11100469 https://www.mdpi.com/2078-2489/11/1 0/469 

[5] Peintner, L., Wintersberger, P., & Riener, A. (2022). Taxonomy of cooperation in automated vehicles: Roles, tasks and HMI structures. _IEEE Transactions on Intelligent Transportation Systems_ , 23(10), 17265–17278. https://doi.org/10.1109/TITS.2021.31 39058 

https://ieeexplore.ieee.org/document /9678531 

10 


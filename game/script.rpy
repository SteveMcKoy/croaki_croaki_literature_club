# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define monika = Character("Frogika")
define sayori = Character("Salyori")
define natsuki = Character("Newtsuki")
define yuri = Character("Toad")
define you = Character("You")

transform n_pos:
    xalign 0.5
    yalign 0.75

transform n_pos_spec1:
    xalign 0.0
    yalign 0.75

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0
# The game starts here.

label start:

    scene wetland 1
    play music "audio/ohayo_sayori.mp3"

    "???" "Heeeeeeyyy!!"
    "I see an annoying girl swimming towards me from the distance, waving her external gills through the water like she's totally oblivious to any attention she might draw to herself."
    "That girl is Salyori, my next-pad neighbor and good friend since we were larvae."
    "You know, the kind of friend you never see yourself making today, but it kind of works out because you've known each other for so long?"
    "We used to swim to school together on days like this, but starting around metamorphosis, she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off swimming away."
    "However, I just sigh and idle in front of a lily pad and let Salyori catch up to me."

    show salyori basic with dissolve
    sayori "Glug glug!"
    sayori "I overslept again!"
    sayori "But I caught you this time!"

    you "Maybe, but only because I decided to stop and wait for you."

    show salyori basic at right with move
    sayori "Gluuuug, you say that like you were thinking about ignoring me!"
    sayori "That's mean!"

    you "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."

    show salyori basic at center with move
    sayori "Fine, fine."
    sayori "But you did wait for me, after all."
    sayori "I guess you don't have it in you to be mean even if you want to~"

    you "Whatever you say, Salyori..."

    sayori "Glug glug~"
    hide sayori basic with dissolve

    "We cross the river together and make our way to the marsh."
    "We amphibans depend on water for almost every part of our lives, so it only makes sense that go to school in a permantly flooded wetland ecosystem."
    "As we draw near, the riverside becomes increasingly speckled with other species making their daily commute."
    "Since she's the only axolotl in the entire school, Salyori draws a lot of attention today as well."
    "By the way, I'm a Japanese Giant, a salamander like Salyori, albiet much more common. Actually, I wonder about that..."

    scene axolotl map with dissolve
    you "Salyori, aren't axolotls only natively found in a single lake in the Valley of Mexico? I mean, your full name is Ambystoma mexicanum... how did you get to suburban Japan, where all dating sims take place?"
    scene wetland 1 with dissolve

    show salyori basic with dissolve
    sayori "Uhhh I dunno, plot convenience I guess. I don't know how I got here, but I was definitly born in Mexico. Look, here's a baby picture!"
    hide salyori basic with dissolve
    scene salyori baby with dissolve
    sayori "Wasn't I cute!"
    scene wetland 1 with dissolve
    show salyori basic with dissolve
    sayori "Anyway, have you decided on a club to join yet?"

    you "A club?"
    you "I told you already, I'm really not intrested in joining any clubs."
    you "I haven't been looking, either."

    show salyori basic with vpunch
    sayori "Glug?! That's not true!"
    sayori "You told me you would join a club this year!"

    you "Did I...?"

    "I'm sure it's possible that I did, in one of our many converastions where I dismissively go along with whatever she's going on about."
    "As you can see, I'm kind of a jerk, especially to literally the only person thats shown me any amount of care or affection."
    "That's probably why I don't have more than one friend tbh. Was there past trauma that made me like this? Should I go to therapy?"
    "Anyway, Salyori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."

    show salyori basic with vpunch
    sayori "Uh-huh!"
    sayori "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    sayori "Your happiness is really important to me, you know!"
    sayori "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    sayori "You trust me, right?"
    sayori "Don't make me keep worring about you..."

    you "Alright, alright..."
    you "I'll look at a few clubs if it makes you happy."
    you "No promises, though."

    sayori "Will you at least promise me you'll try a little?"

    you "Yeah, I guess I'll promise you that."

    sayori "Glug glug!"

    "Wow, it seems like my only friend really cares for me."
    "Still gonna dismiss her every word tho lol."
    "More than that, I'm suprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want ot ease her mind at least a little bit- even if she does exaggerate everything inside of her head."

    hide salyori basic with dissolve
    show wetland 3 with dissolve
    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the at the reeds, looking for an ounce of motivation."

    you "Clubs..."

    "Salyori wants me to pick out some clubs."
    "I guess I have no choice but to start with the anime club..."

    sayori "Hellooo?"
    show salyori basic with dissolve

    you "Salyori...?"

    "Salyori must have swam into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."

    sayori "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    sayori "Honestly, you're even worse than me sometimes... I'm impressed!"

    you "You don't need to wait up for me if it's going to make you late to your own club."

    sayori "Well, I thought you might need some encouragement, so I thought, you know..."

    you "Know what?"

    sayori "Well, that you you could come to my club!"

    "I sigh heavily, which is a strange feeling as although I do have lungs, I mostly breath through my skin using the rich supply of capillaries located there."

    you "Salyori..."

    sayori "Glug?"

    you "...There is no way I'm going to your club."

    show salyori basic with vpunch
    sayori "Gluuuuuggg?! Meanie! You know, you were supposed to have grown another heart chamber since you were a larva, but I guess you've stayed as hearless as ever!"

    "..."
    "Salyori is vice president of the Literature Club."
    "I don't know if anyonw in the school can read, but that's just how it is."
    "Not that I was ever aware that she had any intrest in literature."
    "In fact, I'm 99\% sure that she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show intrest after the one who proposed the club, she inherited the title of \"Vice President\"."
    "That said, my intrest in literature is guarenteed to be even less."
    "Buuuut..."

    you "Alright, in the original game it takes a lot longer to convince me, but we need to speed the plot up in this version so I'll just agree to join."

    sayori "Glug glug! Let's go~"
    hide salyori basic with dissolve
    scene wetland 4 with dissolve
    stop music fadeout 1

    "And thus, today marks the day I sold my soul for plot convienience."
    "I dejectedly follow Salyori across the marsh and upstream- a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Salyori, full of energy, pushes past the reeds into the club room."

    play music "audio/okay_everyone.mp3"
    scene wetland 5 with dissolve
    sayori "Everyone! The new member is here!"

    "Eh? I glance around the room."

    show toad basic with dissolve
    "Girl 1" "Welcome to the Literature Club. It's a pleasure meeting you."
    "Girl 1" "Salyori always says nice things about you."
    hide toad basic with dissolve

    show newtsuki basic at n_pos with dissolve:
    "Girl 2" "Seriously? You brought a boy?"
    "Girl 2" "Way to kill the atmostphere."
    hide newtsuki basic with dissolve

    show frogika basic with dissolve
    "Girl 3" "Ah, you! What a nice suprise!"
    "Girl 3" "Welcome to the club!"
    hide frogika basic with dissolve

    you "..."

    "All words escape me in this situation."
    "This club..."
    "Has worst girl Newtsuki in it!! I want to head out."

    show newtsuki basic at n_pos with dissolve
    "Girl 2" "What are you looking at?"
    "Girl 2" "If you want to say something, say it."

    you "S-Sorry..."

    "I was not sorry."

    show toad basic at right with dissolve
    "Girl 1" "Newtsuki..."

    natsuki "Hmph. Baka. It's not like I like you or anything. That's it, that's my entire character."

    show salyori basic at left with dissolve
    sayori "You can just ignore her when she gets like this~"

    "Salyori says that quietly into my tympanic membrane, then turns back toward the other girls."

    sayori "Anyway! This is Newtsuki, always an annoying bra- I mean full of energy."
    sayori "And this is Toad, the smartest in the club!"

    show toad basic with vpunch
    play sound "audio/toad_yeow.wav"
    yuri "D-don't say things like that..."

    "Toad, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Salyori and Newtsuki."
    "Also, she's a mario character."
    "If I had to guess why, it's because Steve couldn't think of a punny amphibian name for her so he just made her character model a joke instead."

    you "Ah... Well, it's nice to meet both of you."

    "No it's not, I'm lying through my teeth. It's only nice to meet Toad."
    hide toad basic with dissolve
    hide newtsuki basic with dissolve

    sayori "And it sounds like you already know Frogika, is that right?"

    show frogika basic with dissolve
    monika "That's right."
    monika "It's great to see you again."

    "Frogika smiles sweetly."
    "We do know each other- well, we rarely talked, but we were in the same class last year."
    "Frogika was probably the most popular girl in class- smart, pretty, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."

    you "Y-You too, Frogika."

    hide frogika basic with dissolve
    sayori "Come sit down! We made room you for you on the lily pad, so you can sit next to me or Frogika."
    sayori "I'll get the cupcakes~"

    show newtsuki basic at n_pos with vpunch
    natsuki "Hey! I made them, I'll get them!"

    sayori "Sorry, I got a little too excited~"

    show toad basic at right with dissolve
    yuri "Then, how about I make some dirty marsh water flavored tea as well?"
    hide salyori basic with dissolve
    hide newtsuki basic with dissolve
    hide toad basic with dissolve

    "Having just swam over here, I have already absorbed a fair bit of dirty marsh water through the drinking patch on my stomach, but I didn't have the heart to decline best girl."
    "As Salyori mentioned, the lily pad has been arranged so that there is one space next to Frogika and one space next to Salyori."
    "Newtsuki and Toad swim over to the edge of the water, where Newtsuki grabs a wrapped tray and Toad pushes past some reeds into the closet space."
    "Still feeling awkward, I take a seat next to Salyori."
    "Newtsuki proudly swims back to the table, tray on back."

    show newtsuki basic at n_pos with dissolve
    natsuki "Okaaay, are you ready?"
    natsuki "Ta-daa!"

    show salyori basic at right with dissolve
    show frogika basic at left with dissolve
    sayori "Glug glug!"

    "Newtsuki lifts the foil off the tray to reaveal a dozen wriggling earthworms covered in frosting decorated to look like little cats."
    "Which is kind of sick, given that a real cat would slaughter us in seconds if present."
    "Way to go, Newtsuki."

    sayori "So cuuuute~!"

    monika "Ribbit! I had no idea you were so good at worm decoration, Newtsuki!"

    natsuki "(happy newt noises). Well, you know."
    natsuki "Just hurry and take one!"

    "Salyori grabs one first, then Frogika. I follow."

    sayori "It's delicious!"

    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the worm around in my \"hand\", looking for the best angle to take a bite."
    "I'm a real connoisseur that way."
    hide frogika basic with dissolve
    hide salyori basic with dissolve
    "Newtsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "Shoot. I don't want to validate her, but I am getting kind of hungry."
    "I finally bite down."
    "The icing is sweet and full of flavor- I wonder is she made it herself."

    you "This is really good."
    you "Thank you, Newtsuki."

    "Curse my polite upbringing."

    show newtsuki basic at n_pos with vpunch
    natsuki "W-Why are you thanking me? It's not like I...!"

    "Oh hey it's the classic tsundere line. How basic."

    natsuki "...Made them for you or anything, baka."

    you "Eh? You technically did. Salyori said it was to celebrate a new mem-"

    natsuki "Well, maybe!"
    natsuki "But not for, y-you know, you! Baka..."

    you "Alright, alright..."
    hide newtsuki basic with dissolve

    "Sorry Newtsuki, but facts don't care about your feelings."
    "Another anime girl destroyed epic gamer style with facts and logic. You love to see it."
    "Toad returns to the pad, carrying a tea set."
    "She carefully places a teachup in front of each of us before setting down the teapot next to the cupcake tray."

    show toad basic at leftish with dissolve
    you "You keep a whole tea set in this classroom?"

    yuri "Don't worry, the teachers gave us permission."
    yuri "After all, doesn't a hot cup of tea help you enjoy a good book?"

    you "Ah... I-I guess..."

    show frogika basic at rightish with dissolve
    monika "Ribbit, don't let yourself get intimidated, Toad's just trying to impress you."

    show toad basic at leftish with vpunch
    play sound "audio/toad_yah.wav"
    yuri "Croak?! T-that's not..."

    "Insulted, Toad looks away."
    "Oh yeah. It's real best girl hours."

    yuri "I meant that, you know..."

    you "I believe you."
    you "Well, tea and reading might not be a pastime for me, but I at least enjoy the tea."

    yuri "I'm glad..."

    "Toad faintly smiles to herself in relief."
    "Frogika raises a nicitating membrane, then smiles at me."

    hide toad basic with dissolve
    show frogika basic at center with move
    monika "So, what made you consider the Literature Club?"

    you "Um..."

    "She's onto me. I was afraid of the question."
    "Something tells me I shouldn't tell Frogika that I was practically dragged here by Salyori."

    you "Well, I havnen't joined any clubs yet, and Salyori seemed really happy here, so..."

    monika "That's okay! Don't be embarrassed!"
    monika "We'll make sure you feel right at home, okay?"
    monika "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"

    you "Frogika, I'm suprised."
    you "How come you decided to start your own club?"
    you "You could probably be a board memebr for any of the major clubs."
    you "Weren't you a leader of the debate club last year?"

    monika "Ribbit, well, you know..."
    monika "To be honest, since we're just a bunch of amphibans in a marsh, we have no real politacal system, so there was nothing to debate."
    monika "I'd much rather take something I personally enjoy and make something special out of it."
    monika "And if it encourages others to get into literature, then I'm fulfilling that dream!"

    show salyori basic at left with dissolve
    sayori "Frogika really is a great leader!"

    show toad basic at right with dissolve
    "Toad also nods in agreement."

    you "Then I'm suprised there aren't more people in the club yet."
    you "It must be hard to start a new club."

    hide salyori basic dissolve
    hide toad basic with dissolve
    monika "You could put it that way."
    monika "Not many people are very intrested in putting all the effort to start something brand new.."
    monika "Especially when it's something that doesn't grab you attenction, lite literature."
    monika "You have to work hard to convice people that you're both fun and worthwile."

    "To be fair, her target audience is, like, 99\% illiterate."

    monika "But it makes school events, like the festival, that much more important."
    monika "I'm confident that we can all really grow this club before we graduate!"
    monika "Right, everyone?"

    show frogika basic at rightish with move
    show salyori basic at leftish with dissolve
    sayori "Yeah!"

    show frogika basic at right with move
    show salyori basic at center with move
    show toad basic at left with dissolve
    yuri "We'll do our best."

    show salyori basic at rightish with move
    show toad basic at leftish with move
    show newtsuki basic at n_pos_spec1 with dissolve
    "You know it!"

    "Everyone enthusiastically agrees."
    "Such different species, all intrested in the same goal..."
    "Frogika must have worked really hard just to find these three."
    "Maybe the true literature is the friends we make along the way."

    monika "Anyway I'd like to make things official."
    monika "Welcome to the literature club!"

    sayori "Glug glug!"

    yuri "Yes, please enjoy yourself while you're here."

    natsuki "If you really just came for the earthworms, I'll cause you severe bodily harm, baka."

    hide newtsuki basic with dissolve
    hide salyori basic with dissolve
    hide toad basic with dissolve
    show frogika basic at center with move
    monika "Okay everyone!"
    monika "I think with that, we can finally end the gam- I mean meeting on a good note."

    stop music fadeout 1
    scene black with dissolve
    play music "audio/dreams_of_love_and_literature.mp3"
    "And with that, the day comes to an end."
    "Literally nothing bad happens after that."
    "I mean, there was this one time Salyori didn't show up on the morning the school festival and when I went to go check on her..."
    "She was just chillin."
    "And yuri brought a knife to school once..."
    "But it turns out she had the teacher's permission and was going to use it in a earthworm preperation lession with Newtsuki, who has a great relationship with her family by the way."
    "Monika did find out that we were living in a game though."
    "But instead of deleting all her friends she learned how to code and is now the world's first virtual computer scientist."
    "As always, Steve doesn't know how to properly end stories, so here's some generic advice that they put at the end of all the kids shows."
    "Remember kids."
    "Books rule, stay in school, and, while you shouldn't do drugs, criminalizing addiction isn't cool."
    "Big Pharma is the root of our countries problem with opiate addicion."
    "..."
    "P.S.- You can find all of my sources in the about section of the main menu."
    "Ok bye."

    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Death")
define p = Character("Paul (Voice on the Phone!)")
define r = Character("Richard")
define t = Character("Tom Friday")
define s = Character("Prince of Darkness")
define m = Character("Janus")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg party city
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    play music "dreams.mp3"
    
    play sound "vibrate.mp3"
    
    "*buzz buzz*"
    
    d "What...what the hell? Oh come on, I'm at work!"
    
    "*buzz buzz BUZZ*"
    
    show grim reaper at center with dissolve
    
    d "Really Paul? Really?! Fine, fine."
    
    d "Dude, what? I'm at work!"
    
    p "Yooo! Grim, what's up buddy?"
    
    d "I just told you what's up! I'm at work, dammit!"
    
    p "Geez, chill out bud! I was just calling to let you know that we're out of milk...again."
    
    d "I just bought some yesterday! God, can't you take care of it? I'm seriously on the clock here."
    
    p "Sorry man, I'm busy working on my novel. Could you make it chocolate? Just stop on your way to the office!"
    
    d "Yeah, yeah. Whatever."
    
    p "Yes! You're the man, broseidon! King of the brocean!"
    
    d "Just don't touch my Marshmallow Mateys, okay? They got stale last time you left them out--Hello?"
    
    play sound "click.mp3"
    
    "*click*"
    
    d "Hello? Great. Good talk."
    
    scene bg party city 2
    with fade
    
    play music "elevator.mp3"
    
    show grim reaper at left with dissolve
    
    d "I wonder if they have candy corn..."
    
    show richard at right with dissolve
    
    r "Hey, can I help you?"
    
    d "Oh finally. I've only been waiting here for, like, an eternity!"
    
    r "Sorry about that. Nice costume!"
    
    d "Costume?" 
    
    d "Anyways, I've been looking for an employee here...I think his name was...Rich? Richard Tabby? Something like that."
    
    r "Uh...what do you need him for?"
    
    d "Just need to have a cat."
    
    d "Er...chat."
    
    r "That's kind of...weird. What about?"
    
    d "Normal stuff."
    
    r "Um..."
    
    d "The weather. Sports? Sports stuff. Yeah. Sorry, one second..."
    
    "Death grabs a scroll from inside his cloak and reads from it."
    
    d "Oh yeah! I'm here for a beanie baby collection that was put up for sale. On the Ebay."
    
    r "The Ebay?" 
    
    r "Uh okay, well...I'm Richard. Already sold the beanie babies to another bidder." 
    
    r "Sorry man."
    
    d "I really wanted that little alligator..."
    
    d "...you're Richard, huh?" 
    
    d "Yeah, I'm not really here to talk beanie babies, as much as it would please me."
    
    r "Okay."
    
    d "You don't seem to get it...do you see what I'm wearing?"
    
    r "Yeah."
    
    d "Okay then, Richie. Still don't get it?"
    
    r "No."
    
    d "I'm Death."
    
    r "Cool."
    
    r "We have more Halloween supplies in the back, if you're interested."
    
    d "Seriously. I am THE Grim Reaper. I'm here to take your soul."
    
    r "Really? That's a bummer."
    
    d "Are you sure you're Richard? This can't be right..."
    
    "Death fumbles around in his cloak for another scroll with a drawing on it."
    
    d "Hmm, I guess it is you."
    
    r "What's this all about?"
    
    d "You've been sniffing way too much glue in the break room. I know this is Party City and the party never stops and all that, but you huffed waaaaay too much, dude."
    
    r "So am I fired? Wait, you're not the manager, are you?"
    
    "Death looks around. There is absolutely no one else in the stupid Party City store."
    
    d "Let's cut to the chase. I'm going to use this here scythe to TAKE YOUR SOUL. Then after that, I'm going to T.G.I. Friday's, because I have another appointment."
    
    d "Plus they have endless appetizers right now..."
    
    d "...and their wings really aren't as bad as people say."
    
    r "So I'm going to die? That blows."
    
    r "And in a {i}Party City?{/i}"
    
    d "Well know this: Hell is not worse than this wretched void."
    
    r "Wait, I'm going to {color=#f00}hell?{/color}"
    
    d "I'm really not supposed to talk this much. Spoiled it for you..."
    
    d "...my bad."
    
    d "Charon is gonna be {i}pissed...{/i}"
    
    label judgement:
        r "That scythe looks kind of dirty...are you seriously going to use that to kill me?"
        menu:
            "Duh. It's my job.":
                hide richard
                play sound "soulsteal.mp3"
                
                d "And that's that."
                
                d "Ew...there's some soul stuck on the end of the blade!"
                
                show grim reaper at right
                
                d "ew ew ew ew ew ew ew ew ew ew"
                
                show grim reaper at center
                
                d "EW!"
                
                show grim reaper at left
                
                d "Thank god it's Friday..."
                
                
                
            "You know what? Nevermind. Forget it.":
                play sound "swoosh.mp3"
                hide grim reaper
                show richard at center
                                                  
                r "....."
    
                r "Wait, are you coming back later?"
                
                r "Hello?"
                jump office
                
    
    scene bg tgi fridays ext
    with dissolve
    
    d "Finally..."
    
    d "It'd be awesome if Guy Fieri was actually here, like in the commercials..."
    
    scene bg tgi fridays
    with dissolve
    
    play music "waves.mp3"
    
    show grim reaper at left with dissolve
    
    d "No way...they have potato skins again?"
    
    d "AND haystack onions?!"
    
    d "I should've come here with Paul last week..."
    
    d "...instead of Chili's for the eightieth freakin' time..."
    
    show tom at right
    
    t "Hey there, fella! Welcome to T.G.I. Fridays! Where the food is good, but the friends are better!"
    
    t "Nice cloak, guy!"
    
    t "If I could pull off that cloak look half as well as you do, well, look out world! {i}You know what I'm saying?{/i}"
    
    t "Anyways, what'll ya have, pal?"
    
    label food:
        d "Oh wow, so many choices!"
        menu:
            "Endless apps, of course! Wings first!":
                show tom at center
            
            "Ummmmm.....po...tato....skins? No, wait...yeah.":
                show tom at center
             
            "Potato skins AND wings, please!":
                show tom at center
            
            "You know what? I'm going to change it up...a side salad, please.":
                show tom at center
            
    t "A fine choice! And a drink?"
    label drink:
        d "Ooooh..."
        menu:
            "Do you guys have Miller High Life?":
                show tom at center
           
            "You guys have any non-alcoholic beer?":
                show tom at center
           
            "Sprite would really hit the spot right about now.":
                show tom at center
           
            "Some milk, for strong bones!":
                show tom at center
           
    t "Got it! You're on a roll today, my man!"
    
    t "I'll be right back with your order!"
    
    hide tom
    
    d "They're always so nice here!"
    
    d "Such a nice change from the hell demons and soul eaters."
    
    d "Those guys suck."
    
    d "Now...might as well do some more work..."
    
    "Death reaches into his cloak's deep pockets..."
    
    d "Where did I put it? {b}For corn's sake!{/b}"
    
    d "Whoa, what's this?"
    
    "Death finds a plane ticket for Casa Bonita!"
    
    "How convenient!"
    
    d "When did I get..."
    
    "Death reads an attached note addressed to him..."
    
    d "Grim: We so appreciate all that you do for us!"
    
    d "You'll always be one of the Horsemen! Love, Pestilence, War, and Famine!"
    
    d "How did they--where did they--{b}oh wow!{/b}"
    
    d "I'm sure they won't mind if I take a little vacation time...for the first time in eons!"
    
    hide grim reaper with dissolve
    
    show tom at right with dissolve
    
    t "Hey bud, looks like your--"
    
    t "{i}Huh?{/i}"
    
    t "Well I'll be gosh darned. He disappeared into thin air."
    
    show tom at right
    
    t "But it looks like he left his...business card?"
    
    "Mr. Grim Reaper--Infernal Acquisitions"
    
    t "Golly, I should give him a call! I've been looking to expand my business horizons...and I will, or my name's not Tom Friday!"
    
    jump casa
    
    
    

    label office:
    scene bg office with dissolve
    
    play music "soixante.mp3"
    
    d "You know, those cups are recyclable, Beelzebub!"
    
    play sound "2demon.mp3"
    
    d "Don't growl at me! Just make the extra effort and wash them out!"
    
    d "And who forget to fill the coffeemaker?!"
    
    d "If the pot is empty, refill it! It's really not that hard!"
    
    play sound "demon.mp3"
    
    d "Don't think I didn't hear that, Steve! Don't make me come over there!"
    
    play sound "1demon.mp3"
    
    show grim reaper at center
    
    d "I shoud've just gone to Friday's..."
    
    "Mr. Reaper! Back so soon?"
    
    d "Not today...ughhhhhhhh."
    
    show grim reaper at left
    
    show princeofdarkness at right
    
    play sound "creepylaugh.mp3"
    
    s "Aren't you supposed to be out hitting your souls quota?"
    
    s "I looked earlier, and we're still missing that Richard Tabby over at..."
    
    s "{i}Party City.{/i}"
    
    s "Oof. Now I can understand why you wouldn't want to head there."
    
    d "It's not Circuit City bad, believe me."
    
    s "Or Golden Corral bad..."
    
    "Death and the Prince of Darkness gag at the thought of such horrid locales..."
    
    d "To be honest, I was there earlier, but..."
    
    d "I kinda felt bad for the guy."
    
    s "Oh, not this again."
    
    d "Yeah, yeah, I know. Death can't have a conscience!"
    
    d "Death can't have his birthday off!"
    
    d "Death can't have his vacation days!"
    
    s "...it's not that bad, Grim!"
    
    d "Well, actually, IT IS!"
    
    s "I mean, we are in hell..."
    
    s "You could get an office in...you know.."
    
    d "NO no no, it's fine...I mean whatever, right?"
    
    d "I'm just surrounded by demons that constantly belittle me."
    
    d "Yesterday, I brought in ham on an olive loaf. Just left it in fridge..."
    
    s "Did you put the sticker on it?"
    
    d "YES, I put a sticker on it, expressly displaying that it was MY sandwich."
    
    d "Of course, I head out to snag some souls and pancakes over at IHOP..."
    
    d "And by the time I came back, GUESS WHAT?!"
    
    s "Ah I get it! Your sandwich was gone."
    
    d "Ding ding ding! 500 points to the Prince of Darkness!"
    
    d "I'm tired of putting in all this hard work, only for it to go unnoticed!"
    
    d "Unappreciated..."
    
    s "I appreciate you, Grim!"
    
    s "I think if you got involved in more office team building, the demons here would be more welcoming."
    
    s "Instead, you always duck out to go hang out with Paul or watch Food Network."
    
    d "I couldn't miss Diners, Drive Ins, and Dives, okay?"
    
    s "Seriously, you might enjoy them! We always have some fun activities planned."
    
    s "Last week we went minigolfing!"
    
    d "What? Are you kidding me?!"
    
    d "Wait, {i}no!{/i}"
    
    d "That's not gonna cut it, Prince! I need more than fun and games!"
    
    d "I need..."
    
    d "...a {b}higher purpose{/b}."
    
    s "Maybe you do need a break..."
    
    s "Exorcise some of your demons."
    
    d "Exorcise?"
    
    s "Sorry, I meant {i}exercise with some of the demons.{/b}"
    
    s "It'd be good for your heart. Minos was doing Zumba!"
    
    s "Hey, what about {i}Soul Cycle?{/i}"
    
    s "You could work WHILE you work out!"
    
    d "I don't think that's--"
    
    s "Just go take a dip in Cocytus, take Cerberus for a walk!"
    
    s "I don't want to see you in the office until you're ready to work again, okay?"
    
    d "I suppose that..I've needed some 'me' time."
    
    show princeofdarkness at center
    
    s "Unpaid, of course."
    
    d "What the hell?!"
    
    s "Indeed." 
    
    hide princeofdarkness
    
    s "Later Grim. Duty calls!"
    
    
    play sound "creepylaugh.mp3"
    
    show grim reaper at center
    
    label decisions:
        d "Well, I guess I should head out..."
        menu:
            "Early retirement...":
                hide grim reaper
                jump home
            
            "Well, I could go home...even though Paul is there.":
                hide grim reaper
                jump home
            
            "Casa Bonita, here I come!":
                hide grim reaper
                jump casa
       

    label home:
    scene bg home
    
    play music "docks.mp3"
    
    show grim reaper at center with dissolve
    
    d "Paul?"
    
    d "Paullllllllll?!"
    
    d "Alone again...what to do..."
    
    show grim reaper at right
    
    d "I could watch some more {i}Cake Wars{/i}..."
    
    show grim reaper at left
    
    d "Or I could go rollerblade again..."
    
    label waste:
    menu:
        "Cake it is!":
            show grim reaper at center
        
        "Roll all night, baby!":
            show grim reaper at center
            
    d "Ahhhhhhhh......"
    
    d "It really doesn't matter...I might as well just sit around and wait for death."
    
    d "Wait, who can kill me of boredom if I'm Death?"
       
    d "................"
    
    d "................"
    
    d "Sooooooo...."
    
    d "Yeah..."
    
    hide grim reaper
    
    show bg home with fade
       
    "To be continued..."
    
    "Seriously."
    
    "Stop reading!"
    
    "Well, I'm leaving."
    
    "You should do the same. The game is done!"
    
    "It's not even funny at this point."
    
    "Later!"
    
    return
    
    label casa:
    scene bg bonita with dissolve
    
    play music "gagool.mp3"
    
    show grim reaper at left with dissolve
    
    d "Soul surfing is my new favorite hobby!"
    
    d "If only I could actually {i}swim{/i} and not just...float."
    
    d "It's hard out here for a specter..."
    
    "Death takes in the warm rays of sunlight in his tropical hideaway."
    
    "Alone, he continues to talk to himself."
    
    d "It's no River Styx, but it was nice and cool water. Not too cool, that would've chilled me straight to the bone!"
    
    d "That's a good one, Death..."
    
    d "Thanks Grim."
    
    "Death really just isn't used to vacation."
    
    "Lost in thought over his vision of Guy Fieri's 'Flavortown,' Death's peace and quiet is shattered by a talking mask!"
    
    show janus at center with dissolve
    
    m "Hey! Hey!"
    
    show grim reaper at right
    
    d "AH!"
    
    show grim reaper at left
    
    d "Holy crap!"
    
    d "Where in Danny Glover's name did you come from?!"
    
    m "Oh, I live here."
    
    m "Usually I don't bother guests..."
    
    d "Could've fooled me!"
    
    m "...but I'm a {b}BIG{/b} fan."
    
    "Death perks up at the thought of having fans."
    
    d "...a fan?"
    
    show janus at right
    
    m "Yep. However, as much as I'd like to talk scythes and surf, we have a massive problem here."
    
    m "You probably didn't notice, but that's totally cool! You're obviously a super busy guy, lots of appearances to make."
    
    d "I don't really deal with problems other than...you know..."
    
    d "Sending souls on their way!"
    
    m "By murdering them with a scythe, I know."
    
    d "HEY! It's not {i}murder!{/i}"
    
    d "It's just a part of the process!"
    
    d "I didn't start the scythe thing, okay?"
    
    d "It's a legacy sort of deal. It's in the contract!"
    
    d "I don't need to explain myself, I came here to relax!"
    
    m "I get that. I just thought you'd be interested in helping me to solve a mystery..."
    
    d "A what?"
    
    m "Ehhhhh it doesn't matter."
    
    m "You're not interested. Just some souls escaping imprisonment."
    
    "Death straightens up and brushes off his cloak."
    
    d "Escaped souls?"
    
    d "......."
    
    d "You know what? Try me, creepy little mask dude."
    
    "To be continued..."
    
    "I swear!"
    
    "Just click through, there's not much more to it."
    
    "Again."
    
    "Okay I'm headed out."
    
    return
    
   
 
            
    
    
                
    
    
    
    

    
    

    # This ends the game.

    return

robots = {
    'robot1' : {'name': 'HeavyArms',
            'health':130,
            'weapon1': {'name': 'Shoulder Missles','attack_power':50,'win':'The MISSLES over powered the Dinosaur','type':'power'},
            'weapon2': {'name': 'Wrist Blade','attack_power':30,'win':'A quick strick from the WRIST BLADE hit its mark','type':'precision'},
            'weapon3': {'name': 'Mini Gun','attack_power':40,'win':'The MINI GUN pummeled the Dinosaur','type':'quick'},
            },
    'robot2' : {'name': 'Deathscythe',
            'health':60,
            'weapon1': {'name': 'Wrist Beam Missle','attack_power':70,'win':'The MISSLE pierced through the Dinsosaur','type':'power'},
            'weapon2': {'name': 'Knee-Strike','attack_power':50,'win':'The KNEE-STRIKE was true','type':'precision'},
            'weapon3': {'name': 'Beam Scythe','attack_power':60,'win':'The SCYTHE sliced the Dinosaur Deep','type':'quick'},
            },
    'robot3' : {'name': 'SandRock',
            'health':100,
            'weapon1': {'name': 'Vulcan Gun','attack_power':60,'win':'The VULCAN GUN\'s bullets find the Dinosaur','type':'power'},
            'weapon2': {'name': 'Cross-Crusher','attack_power':40,'win':'The CROSS-CRUSHER latched on to the Dinosaur','type':'precision'},
            'weapon3': {'name': 'Heated Blades','attack_power':50,'win':'The Dinosaur was burned badly by the HEATED BLADES','type':'quick'},
            },
}


dinosaurs = {
    'dinosaur1' : {'name': 'T-Rex','health':100, 'attack_power': 50, 
                'attack1': {'name': 'Tail Swipe','attack_power':10,'win':'The T-Rex\'s TAIL powered into the Robot','type':'power'},
                'attack2': {'name': 'Bite','attack_power':-10,'win':'The T-Rex\'s BITE crushed a weak point','type':'precision'},
                'attack3': {'name': 'Claws','attack_power':0,'win':'The T-Rex\'s tiny CLAWS caught and threw the projectile back','type':'quick'},
},
    'dinosaur2' : {'name': 'Triceratops','health':130, 'attack_power': 40,
                'attack1': {'name': 'Tail Swipe','attack_power':10,'win':'The Triceratop\'s TAIL powered into the Robot','type':'power'},
                'attack2': {'name': 'Stomp','attack_power':-10,'win':'The Triceratop STOMPPED his Robot back','type':'precision'},
                'attack3': {'name': 'Spike Head-Butt','attack_power':0,'win':'The Triceratop\'s SPIKE struck true','type':'quick'},
},
    'dinosaur3' : {'name': 'Terradactyl','health':60, 'attack_power': 60,
                'attack1': {'name': 'Nose Dive','attack_power':10,'win':'The Terradactyl\'s DIVE pierced the Robot','type':'power'},
                'attack2': {'name': 'Wing Gust','attack_power':-10,'win':'The Terradactyl\'s GUST hit the Robot back','type':'precision'},
                'attack3': {'name': 'Scratch','attack_power':0,'win':'The Terradactyl\'s claws SCRATCHED deep','type':'quick'},
},

}
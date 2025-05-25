import os
import sys
import requests
import time
import random as rng

clear = lambda: os.system('cls')
clear()
bn = "b260525"
title = f"CC {bn}"
build = f"Complex Cat - A SimpleMMO Companion Applet {bn}"
os.system(f'title,{title}')
print(f"Welcome to {build}\nWe hope to help you play smarter.\n\nIn order to use this applet, be sure that you are: \n- Logged in on the Web App [https://web.simple-mmo.com/] \n- and have access to the API features.\n\nGet your API Key from the link below:\n[ https://web.simple-mmo.com/p-api/home ]" )
api_input = input()
api_key = api_input
clear()

current_time = time.gmtime()
time_int = time.time()
formatted_time = time.strftime("%A, %d %B, %Y | %X", current_time)


notice = f"⚠️ | You may risk suspension of your API token, if you navigate this program too fast.\nCurrent rules for API use is 40 calls per minute.\n\n⚠️ | Accessing Guild Features, without a guild, may crash the program."
nf = "{:,}"
command_menu = "Application Menu:\n1. Information (New? Read this first)\n\nGuild Features:\n2. Leaderboard (2 API calls)n\n3. In-depth Guild View (3 API calls)\n4. Guild Difference Calculator (3 API calls)\n\nPlayer Features (no guild):\n5. Player Data View (1 API calls)\n6. Personal Data View (Statistics) (1 API call)\n7. Cheapest Diamond Listing (2 API calls)\n8. Battle Arena Gold Requirements (1 API call)\n9. Skilling Average Calculator (1 API call)\n10. Sprint Time Calculator (0 API calls)\n\n0. Quit"
warn_menu = "⚠️ | Press 0 to pass this step."
def information():
    print(build)
    print(f"\nBuild Number: {bn}")
    print(f"Developer: Fleuren")
    print(f"\nThis program is made to work alongside the following clients:\n\nWeb App: https://web.simple-mmo.com/\nApp Hub: https://smmo-hub.com/\niOS Client: https://apps.apple.com/us/app/simplemmo-mmorpg-pvp-rpg/id1606898406\nAndroid Client: https://play.google.com/store/apps/details?id=dawsn.simplemmo&hl=en&pli=1\nThis program only pulls data from the public API.\n")
    print(f"View changes, functions in development, and releases at: https://github.com/fleuren/smmo-api-projects\n")
    print(f"Features:\n[ Seasonal Guild Leaderboard ]\nPrints the Seasonal Guild Leaderboard for the current season.\n\n[ In-depth Guild View ]\nView specific details about a certain guild (requires guild ID, which can be found in the leaderboard.\n\n[ Player Data View ]\nPrints data from a specific user (similar to Personal Data View). Requires a Player's UID, which is found at the bottom of their stats page\n[ Guild Difference Calculator ]\nCalculates the difference in Guild EXP between your guild, and an opponent's guild.\n\n[ Personal Data View ]\nDisplays some of your personal data.\n\n[ Cheapest Diamond Listing ]\nLists the cheapest diamond price, and calculates how much you can buy with your current pocket gold.\n\n[ Battle Arena Gold Requirement Calculator ]\nCalculates how much gold you require, depending on your current energy points.)\n\n[ Skilling Average Calculator]\nCalculates the average of your player skills (mining, treasurehunting, fishing, woodcutting, and crafting)\n\n[ Sprint Time Calculator ]\nCalculates the time it will take for you to finish a sprint, along with the time it takes to refill (assuming that you don't spend points anywhere else)")
    print(f"\nBinx loves you!")
    print(f"Built using Python 3.10")

    print(f"\n{notice}")
    print(command_menu)
    command = int(input())
    menu(command)
    print(f"⚠️ | This program may slow-down during the usage of some features, depending on your device's performance, the calculations being done, or just general code jank - sorry for this one :p")
def sgl():
    currentseason_endpoint = f'https://api.simple-mmo.com/v1/guilds/seasons?api_key={api_key}'
    currentseason_response = requests.post(currentseason_endpoint)
    for i in range(500):
            try:
                season_id = currentseason_response.json()[i]['id']
            except:
                continue
    print(build)
    print(f"Leaderboard for Season {season_id}\n")
    seasonLB_endpoint = f'https://api.simple-mmo.com/v1/guilds/seasons/{season_id}?api_key={api_key}'
    seasonLB_response = requests.post(seasonLB_endpoint)
    def sgl_print(min_placement, max_placement):
        clear()
        print(build)
        for i in range(min_placement,max_placement):
            sgl_pos = seasonLB_response.json()[i]['position']
            sgl_id = seasonLB_response.json()[i]['guild']['id']
            sgl_name = seasonLB_response.json()[i]['guild']['name']
            sgl_exp = seasonLB_response.json()[i]['experience']
            print(f"•\t{sgl_pos} | {sgl_id} | {sgl_name}\n\tExperience: {nf.format(sgl_exp)}\n")
        print("Look at another tier, or go back to menu:")
        print("Select a tier:\n1. Celestial (1-5)\n2. Legendary (6-10)\n3. Epic (11-15)\n4. Elite (16-20)\n5. Epic (21-25)\n6. All\n\n0. Back to menu\n")
        sgl_menu = int(input())
        sglbrackets(sgl_menu)
    def sglbrackets(sgl_menu):
        match sgl_menu:
            case 1:
                min_placement = 0
                max_placement = 5
                sgl_print(min_placement, max_placement)
            case 2:
                min_placement = 5
                max_placement = 10
                sgl_print(min_placement, max_placement)
            case 3:
                min_placement = 10
                max_placement = 15
                sgl_print(min_placement, max_placement)
            case 4:
                min_placement = 15
                max_placement = 20
                sgl_print(min_placement, max_placement)
            case 5:
                min_placement = 20
                max_placement = 25
                sgl_print(min_placement, max_placement)
            case 6:
                min_placement = 0
                max_placement = 50
                sgl_print(min_placement, max_placement)
            case _:
                clear()
                print(build)

                print(command_menu)
                command = int(input())
                menu(command)

    print("Select a tier:\n1. Celestial (1-5)\n2. Legendary (6-10)\n3. Epic (11-15)\n4. Elite (16-20)\n5. Epic (21-25)\n6. All\n\n0. Back to menu")
    sgl_menu = int(input())
    sglbrackets(sgl_menu)
    
    print(command_menu)
    command = int(input())
    menu(command)
def guild_specific(gs_id):
    gs_warrior = 0
    gs_safe = 0
    clear()
    print(build)
    
    gs_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{gs_id}?api_key={api_key}'
    gs_response = requests.post(gs_endpoint)
    gsx_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{gs_id}?api_key={api_key}'
    gsx_response = requests.post(gsx_endpoint)
    gs_name = gs_response.json()['name']
    gs_membercount = gs_response.json()['member_count']
    gs_ownerid = gs_response.json()['owner']
    gs_exp = gs_response.json()['current_season_exp']
    gs_war = gs_response.json()['eligible_for_guild_war']
    print(f"In-depth Guild view for: {gs_name}\n")
    
    for i in range (gs_membercount):
        member_warrior = gsx_response.json()[i]['warrior']
        member_safe = gsx_response.json()[i]['safe_mode']
        if member_warrior == 1:
            gs_warrior += 1
        if member_safe == 1:
            gs_safe += 1
    
    ownerid_endpoint = f'https://api.simple-mmo.com/v1/player/info/{gs_ownerid}?api_key={api_key}'
    ownerid_response = requests.post(ownerid_endpoint)
    
    online = 0
    offline = 0
    gs_owner = ownerid_response.json()['name']
    for i in range (gs_membercount):
        member_id = gsx_response.json()[i]['user_id']
        member_name = gsx_response.json()[i]['name']
        member_level = gsx_response.json()[i]['level']
        member_role = gsx_response.json()[i]['position']
        member_safe = gsx_response.json()[i]['safe_mode']
        member_warrior = gsx_response.json()[i]['warrior']
        member_inactive = gsx_response.json()[i]['last_activity']
        current_time = time.time()
        days_inactive1 = current_time-member_inactive
        days_inactive2 = days_inactive1/300
        days_inactive_int = int(days_inactive2)
        days_inactive_readable = str

        if days_inactive_int == 0:
            days_inactive_readable = "Active / Active less than a day ago"
            online += 1
        elif days_inactive_int == 1:
            days_inactive_readable = f"Inactive for {days_inactive_int} day."
            offline += 1
        else:
            days_inactive_readable = f"Inactive for {days_inactive_int} days."
            offline += 1
        safe_readable = str
        warrior_readable = str
        if member_safe == 1:
            safe_readable = "🔷"
        else:
            safe_readable = "🔶"

        
        if member_warrior == 1:
            warrior_readable = "🔪"

        else:
            warrior_readable = "🌱"
    print(f'Name\t | {gs_name}\nLeader\t | {gs_owner}\n\nMember/s:  {gs_membercount} | Warriors: {gs_warrior} | In safe mode: {gs_safe}\n🟢 (within 5 minutes): {online} members | 🔴 : {offline} members\nCan participate in war: {gs_war}\n\nExp | {nf.format(gs_exp)}')
    print(f'\nExtra info (in-game guild webpage):\nhttps://web.simple-mmo.com/guilds/view/{gs_id}?new_page=true\n')
    print("In-depth Guild Menu:\n1. See Guild Members\n0. Back to menu:")
    gs_menu = int(input())
    if gs_menu == 1:
            clear()
            print(build)
            print(f'Guild Members of {gs_name}:\nSafe Mode: 🔷/🔶 | Warrior: ⚔️/🌱\n')
            for i in range (gs_membercount):
                member_id = gsx_response.json()[i]['user_id']
                member_name = gsx_response.json()[i]['name']
                member_level = gsx_response.json()[i]['level']
                member_role = gsx_response.json()[i]['position']
                member_safe = gsx_response.json()[i]['safe_mode']
                member_warrior = gsx_response.json()[i]['warrior']
                member_inactive = gsx_response.json()[i]['last_activity']
                current_time = time.time()
                days_inactive1 = current_time-member_inactive
                days_inactive2 = days_inactive1/86400
                days_inactive_int = int(days_inactive2)
                days_inactive_readable = str
                if days_inactive_int == 0:
                    days_inactive_readable = "Active / Active less than a day ago"
                    
                elif days_inactive_int == 1:
                    days_inactive_readable = f"Inactive for {days_inactive_int} day."
                    
                else:
                    days_inactive_readable = f"Inactive for {days_inactive_int} days."
                    


                print(f"Name: {member_name} | {warrior_readable}{safe_readable} | {member_id}\nLevel: {nf.format(member_level)} | Position: {member_role}\nActivity (in days): {days_inactive_readable} \n")

            print(command_menu)
            command = int(input())
            menu(command)
    elif gs_menu != 1:
        clear()
        print(build)

        print(command_menu)
        command = int(input())
        menu(command)


def player_stats(player_id):
    clear()
    print(build)
    playerinfo_endpoint = f'https://api.simple-mmo.com/v1/player/info/{player_id}?api_key={api_key}'
    playerinfo_response = requests.post(playerinfo_endpoint)

    pl_id = playerinfo_response.json()['id']
    pl_name = playerinfo_response.json()['name']
    pl_lvl = playerinfo_response.json()['level']
    pl_gold = playerinfo_response.json()['gold']
    pl_step = playerinfo_response.json()['steps']
    pl_npc = playerinfo_response.json()['npc_kills']
    pl_pvp = playerinfo_response.json()['user_kills']
    pl_quest = playerinfo_response.json()['quests_complete']
    pl_st = playerinfo_response.json()['str']
    pl_df = playerinfo_response.json()['def']
    pl_dx = playerinfo_response.json()['dex']
    pl_bst = playerinfo_response.json()['bonus_str']
    pl_bdf = playerinfo_response.json()['bonus_def']
    pl_bdx = playerinfo_response.json()['bonus_dex']
    pl_hp = playerinfo_response.json()['hp']
    pl_maxhp = playerinfo_response.json()['max_hp']
    pl_area = playerinfo_response.json()['current_location']['name']
    pl_active = playerinfo_response.json()['last_activity']

    print(f"User info of: {pl_name} | {pl_id}")
    print(f"{pl_name} | Level: {nf.format(pl_lvl)}\nLocation: {pl_area}\nPocket Gold: {nf.format(pl_gold)}")
    print(f"Health: {nf.format(pl_hp)}/{nf.format(pl_maxhp)}")
    print(f"Steps: {nf.format(pl_step)} | NPC: {nf.format(pl_npc)} | PVP: {nf.format(pl_pvp)}")
    print(f"STR: {nf.format(pl_st+pl_bst)} | DEF: {nf.format(pl_df+pl_bdf)} | DEX: {nf.format(pl_dx+pl_bdx)}")
    print(f"Quests completed: {nf.format(pl_quest)}")
    pl_active_now = time_int-pl_active
    if pl_active_now <= 300:
        active_status = "Active now"
    else:
        active_gmtime = time.gmtime(pl_active)
        active_status = time.strftime("%A, %d %B, %Y | %X", active_gmtime)
    print(f"Activity: {active_status} ")

    

    print(command_menu)
    command = int(input())
    menu(command)
def guildTarget(target_id):
    clear()
    print(build)
    warrior_count = 0
    const_npc = 20
    const_pvp = 130
    const_step = 3
    

    targetinfo_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{target_id}?api_key={api_key}'
    targetinfo_response = requests.post(targetinfo_endpoint)
    host_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    host_response = requests.post(host_endpoint)

    host_guild = host_response.json()['guild']['id']
    host_name = host_response.json()['guild']['name']

    yourguild_endpoint = f'https://api.simple-mmo.com/v1/guilds/info/{host_guild}?api_key={api_key}'
    yourguild_response = requests.post(yourguild_endpoint)    
    yourguildmember_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{host_guild}?api_key={api_key}'
    yourguildmmeber_response = requests.post(yourguildmember_endpoint)

    target_name = targetinfo_response.json()['name']
    target_exp = targetinfo_response.json()['current_season_exp']

    host_name = yourguild_response.json()['name']
    host_exp = yourguild_response.json()['current_season_exp']
    host_members = yourguild_response.json()['member_count']
    difference = target_exp-host_exp
    if difference <= -1:
        difference = 0

    for i in range (host_members):
        member_warrior = yourguildmmeber_response.json()[i]['warrior']
        if member_warrior == 1:
            warrior_count += 1
    print(f"Guild Difference Calculator | {target_name} vs. {host_name}\n")
    print(f"Target Guild: {target_name}\nExperience: {nf.format(target_exp)}\n")
    print(f"Your Guild: {host_name}\nExperience: {nf.format(host_exp)}\n")
    print(f"Members: {host_members} | Warriors: {warrior_count}\n")
    print(f"Difference / Target: {nf.format(difference)}\n")
    stepstotal = int(difference/const_step)
    npctotal = int(difference/const_npc)
    pvptotal = int(difference/const_pvp)

    stepsper = int(stepstotal/host_members)
    npcper = int(npctotal/host_members)
    pvpper = int(pvptotal/warrior_count)

    print(f"Total Steps Needed: {nf.format(stepstotal)}\nTotal NPC Kills needed: {nf.format(npctotal)}\nTotal PVP Kills needed: {nf.format(pvptotal)}\n")
    print(f"Steps per member: {nf.format(stepsper)}\nNPC Kills per member: {nf.format(npcper)}\nPVP kills per warrior: {nf.format(pvpper)} | Warriors: {warrior_count}")
    print(f"\nNote that this only calculates for the snapshot taken at the time of: {formatted_time}")


    print(f"\n{command_menu}")
    command = int(input())
    menu(command)
def playerData():
    clear()
    print(build)
    playerData_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    playerData_response = requests.post(playerData_endpoint)

    name = playerData_response.json()['name']
    level = playerData_response.json()['level']
    location = playerData_response.json()['current_location']['name']
    guild = str
    currentqp = playerData_response.json()['quest_points']
    maxqp = playerData_response.json()['maximum_quest_points']
    currentep = playerData_response.json()['energy']
    maxep = playerData_response.json()['maximum_energy']
    gold = playerData_response.json()['gold']
    steps = playerData_response.json()['steps']
    diamonds = playerData_response.json()['diamonds']
    health = playerData_response.json()['hp']
    totalhealth = playerData_response.json()['max_hp']
    healthdiff = totalhealth-health
    safe = playerData_response.json()['safeMode']
    npc = playerData_response.json()['npc_kills']
    pvp = playerData_response.json()['user_kills']
    st = playerData_response.json()['str']
    df = playerData_response.json()['def']
    dx = playerData_response.json()['dex']
    bst = playerData_response.json()['bonus_str']
    bdf = playerData_response.json()['bonus_def']
    bdx = playerData_response.json()['bonus_dex']
    
    tst = st+bst
    tdf = df+bdf
    tdx = dx+bdx

    while True:
        try:
            guild = playerData_response.json()['guild']['name']
            break
        except KeyError:
            guild = "No Guild"
            break
    if healthdiff == 0:
        diff = ""
    else:
        diff = f" | 🩹 : {nf.format(healthdiff)} damage taken."

    if safe == 1:
        kills = f" | NPC 🔪 : {nf.format(npc)}"
    else:
        kills = f" | NPC 🔪 : {nf.format(npc)} | PVP 🔪 : {nf.format(pvp)} "
    print(f"\nProfile:\n{name} | Lv: {nf.format(level)} | Guild: {guild}\nLocation: {location}\n⚡: {currentep} / {maxep} | 💫: {currentqp} / {maxqp}\n🪙: {nf.format(gold)} | 💎: {nf.format(diamonds)}\n❤️: {nf.format(health)}/{nf.format(totalhealth)}{diff}\n🏃: {nf.format(steps)}{kills}")
    print(f"\nStats:\nSTR: {nf.format(tst)} | DEF: {nf.format(tdf)} | DEX: {nf.format(tdx)}")

    print(f'\n{command_menu}')
    command = int(input())
    menu(command)
def cheapestdiamond():
    clear()
    print(build)
    diamond_market_endpoint = f'https://api.simple-mmo.com/v1/diamond-market?api_key={api_key}'
    diamondmarket_response = requests.post(diamond_market_endpoint)
    playerData_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    playerData_response = requests.post(playerData_endpoint)

    gold = playerData_response.json()['gold']
    for i in range(1000):
        try:
            seller = diamondmarket_response.json()[i]['seller']['name']
            remaining = diamondmarket_response.json()[i]['diamonds_remaining']
            price = diamondmarket_response.json()[i]['price_per_diamond']
        except:
            continue
    buyable = int(gold/price)
    if buyable > remaining:
        buyable = remaining
    cost = int(buyable*price)
    goldremaining = int(gold-cost)
    print(f"Cheapest listing as of {formatted_time} is:")
    print(f"\n💎: {remaining} diamond/s\n🪙: {nf.format(price)} per diamond.\n\nSold by: {seller}")
    print(f"\n[ RECEIPT ]")
    print(f"With current prices, you can buy {buyable} diamond/s.")
    print(f"Your pocket gold: {nf.format(gold)}\nCost: {nf.format(cost)}")    
    print(f"Remaining Gold: {nf.format(goldremaining)}")

    print(f'\n{command_menu}')
    command = int(input())
    menu(command)
def arenagold():
    clear()
    print(build)
    playerData_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    playerData_response = requests.post(playerData_endpoint)

    copper = 1000
    bronze = 2500
    silver = 6000
    gold = 9375
    platinum = 11250
    titanium = 13750
    circle = 16250
    ragnarok = 18750
    olympus = 21250
    rapture = 27000
    nirvana = 34500

    energy = playerData_response.json()['energy']

    reqcopper = copper*energy
    reqbronze = bronze*energy
    reqsilver = silver*energy
    reqgold = gold*energy
    reqplatinum = platinum*energy
    reqtitanium = titanium*energy
    reqcircle = circle*energy
    reqragnarok = ragnarok*energy
    reqolympus = olympus*energy
    reqrapture = rapture*energy
    reqnirvana = nirvana*energy
    print("Battle Arena Gold Calculations:\n")
    print(f"Gold Requirements for each tier. With your current energy points of {energy}\n")
    print("[ 🔴 ]")
    print(f"Copper League: {nf.format(reqcopper)}🪙")
    print(f"Bronze League: {nf.format(reqbronze)}🪙")
    print(f"Silver League: {nf.format(reqsilver)}🪙\n")
    print("[ 🟡 ]")
    print(f"Gold League: {nf.format(reqgold)}🪙")
    print(f"Platinum League: {nf.format(reqplatinum)}🪙")
    print(f"Titanium League: {nf.format(reqtitanium)}🪙\n")
    print("[ 🟢 ]")
    print(f"The 7th Circle: {nf.format(reqcircle)}🪙")
    print(f"Ragnarok: {nf.format(reqragnarok)}🪙")
    print(f"Mount Olympus: {nf.format(reqolympus)}🪙\n")
    print("[ 🔵 ]")
    print(f"Rapture: {nf.format(reqrapture)}🪙\n")
    print("[ 🟣 ]")
    print(f"Nirvana: {nf.format(reqnirvana)}🪙\n")


    print(command_menu)
    command = int(input())
    menu(command)
def skillingcalc():

    personal_endpoint = f'https://api.simple-mmo.com/v1/player/me?api_key={api_key}'
    personal_response = requests.post(personal_endpoint)
    my_name = personal_response.json()['name']
    my_uid = personal_response.json()['id']
    skillcalc_endpoint = f'https://api.simple-mmo.com/v1/player/skills/{my_uid}?api_key={api_key}'
    skillcalc_response = requests.post(skillcalc_endpoint)

    mining          = skillcalc_response.json()[2]['skill']
    mininglv        = skillcalc_response.json()[2]['level']

    treasure        = skillcalc_response.json()[0]['skill']
    treasurelv      = skillcalc_response.json()[0]['level']

    fishing         = skillcalc_response.json()[3]['skill']
    fishinglv       = skillcalc_response.json()[3]['level']

    woodcutting     = skillcalc_response.json()[1]['skill']
    woodcuttinglv   = skillcalc_response.json()[1]['level']

    crafting        = "Crafting"
    craftinglv      = skillcalc_response.json()[5]['level']

    print(f"Details for User: {my_name} | ID: {my_uid}\n")
    print(f"Your Skilling Average (SL Score): {nf.format(mininglv+fishinglv+woodcuttinglv+craftinglv+treasurelv / 5)}")
    print("[ Your Skills ]\n")
    print(f"⛏️: {mining.capitalize()} Level: {nf.format(mininglv)}")
    print(f"🪙: {treasure.capitalize()}  Level: {nf.format(treasurelv)}")
    print(f"🎣: {fishing.capitalize()} Level:{nf.format(fishinglv)}")
    print(f"🪓: {woodcutting.capitalize()} Level:{nf.format(woodcuttinglv)}")
    print(f"⚒️: {crafting} Level: {nf.format(craftinglv)}")


    

    print(command_menu)
    command = int(input())
    menu(command)
def sprinttimer():
    print("How much energy/minutes would you like to spend?")
    energySpent = int(input())
    clear()
    print(build)
    currentTimeUnix = time.time()
    currentTimeGMTime = time.gmtime(currentTimeUnix)
    currentGMT = time.strftime("%A, %d %B, %Y | %X", currentTimeGMTime)
    print(f"\nCurrent time: {currentGMT}")

    print(f"\nYour energy point/s: {energySpent}")
    energyToSprintEnd = int(energySpent*60)
    energyTimeToRefill = int(energySpent*300)
    refillInMinutes = int(energyTimeToRefill/60)
    totalTimeUnix = int(currentTimeUnix+energyToSprintEnd)
    totalTimeGMTime = time.gmtime(totalTimeUnix)
    refillTime = int(currentTimeUnix+energyTimeToRefill)
    refillTimeGMTime = time.gmtime(refillTime)
    sprintGMT = time.strftime("%A, %d %B, %Y | %X", totalTimeGMTime)
    refillGMT = time.strftime("%A, %d %B, %Y | %X", refillTimeGMTime)

    print(f"When your sprint ends: {sprintGMT}")
    print(f"Refilled on: {refillGMT}")
    print(f"You will be sprinting for: {energySpent} minute/s")
    print(f"{energySpent} point/s will be refilled in {refillInMinutes} minute/s")

    print(f'\n{command_menu}')
    command = int(input())
    menu(command)
def menu(command):
    clear()
    match command:
        case 1:
            information()
        case 2:
            sgl()
        case 3:
            clear()
            print(build)
            print(f"✒️ | Input the ID of the guild you'd like to take a further look into.")
            print(warn_menu)
            guild_id = int(input())
            if guild_id == 0:
                clear()
                print(build)

                print(command_menu)
                command = int(input())
                menu(command)
            else:
                guild_specific(guild_id)
        case 4:
            clear()
            print(build)
            print("✒️ | What's your target guild (Guild ID Needed)?")
            print(warn_menu)
            target_id = int(input())
            if target_id == 0:
                clear()
                print(build)

                print(command_menu)
                command = int(input())
                menu(command)
            else:
                guildTarget(target_id)
        case 5:
            clear()
            print(build)
            print("✒️ | Which player would you like to check (input ID):")
            print(warn_menu)
            player_id = int(input())
            if player_id == 0:
                clear()
                print(build)

                print(command_menu)
                command = int(input())
                menu(command)
            else:
                player_stats(player_id)

        case 6:
            clear()
            print(build)
            playerData()
        case 7:
            clear()
            print(build)
            cheapestdiamond()
        case 8:
            clear()
            print(build)
            arenagold()
        case 9:
            clear()
            print(build)
            skillingcalc()
        case 10:
            clear()
            print(build)
            sprinttimer()
        case 0:
            print(build)
            print("Goodbye ! 👋")
            print("You're beautiful, and capable of many things. . .")
            time.sleep(1)
            sys.exit()
        case _:
            print(build)
            print("⚠️ | Invalid command detected, please enter a valid command")
            print(command_menu)
            command = int(input())
            menu(command)

print(build)
print(f"\n{notice}\n")
print(command_menu)
command = int(input())
menu(command)

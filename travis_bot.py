import discord,asyncio,os
from discord.ext import commands
from datetime import date

bot = commands.Bot(command_prefix = '!')
id = bot.get_guild(684446737313955871)

@bot.event
async def on_ready():
    print('Bot is ready')

#add new task
@bot.command()
async def add(ctx, task):
    with open('tasks.txt') as f:    
        task_list = f.read().splitlines()
        f.close()

    if task in task_list:
        await ctx.send('Task "{}" already in the burndown chart'.format(task))
    else:
        await ctx.send('Task "{}" is being added to burndown chart'.format(task))
        with open('tasks.txt', 'w') as f:
            for task1 in task_list:
                f.write('{}\n'.format(task1))

            f.write('{}'.format(task))
            task_list1 = f.read().splitlines()
            f.close()
        print (task_list1)

#list all tasks
@bot.command()
async def tasks(ctx):
    await ctx.send('Here are all the tasks currently on the burndown chart')
    with open('tasks.txt') as f:    
        task_list = f.read().splitlines()
        f.close()

    i = 1 
    for task in task_list:
        await ctx.send('{}. {}'.format(i, task))
        i+=1

@bot.command()
async def burndown_help(ctx):
    await ctx.send('!tasks -> lists all the tasks in chart')
    await ctx.send('!log task time -> adds task to the burndown (task = task name, time = units)')
    await ctx.send('!add -> adds new task to burndown chart')

#log time for task
@bot.command()
async def log(ctx, task, time):
    with open('tasks.txt') as f:    
        task_list = f.read().splitlines()
        f.close()

    with open('burndownlog.txt') as f:    
        log_list = f.read().splitlines()
        f.close()


    if (not(task in task_list)) or not(time.isdigit()):
        await ctx.send('You made a mistake, try again')
    else:
        await ctx.send ('You logged {} units for task "{}"'.format(time, task))
        with open('burndownlog.txt', 'w') as f:    
            for log in log_list:
                f.write('{}\n'.format(log))
            f.write('{}_{}_{}'.format(date.today(),task,time))
            f.close()

@bot.command()
async def status(ctx):
    await ctx.send('Fetching info from github')
    await ctx.send('Fetch error')

bot.run('Njg0NzA3ODA0NTk0MTc2MTI2.Xl-fgg.8eJWa36qMbFH6-AQW672X5hmYcI')
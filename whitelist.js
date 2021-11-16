const Discord = require("discord.js");
const client = new Discord.Client()

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
  client.user.setActivity("Made by Aesurgam ... RIP LolZ", {
  type:"PLAYING",
});
})



client.on("message", msg => {
  if(msg.author.id == "censored") {
   if(msg.content == "!on") {
     channel = msg.channel
    channel.bulkDelete(25)
  .then(messages => channel.send(`Channel barrier of ${messages.size} messages size has been cleared. This channel can now be used again!`))
  .catch(console.error);
}}})
client.on("message", msg =>{
  if (msg.content=== "R") {
    msg.react('😔')
  }else if (msg.content == "r") {
    msg.react("🥶")
  }else if(msg.content == "!hw") {
    msg.reply("cesnored")

  }else if(msg.author.id == "censored") {
    if(msg.content == "!off") {
    const channel = msg.channel
    channel.bulkDelete(5)
  .then(messages => channel.send(`Bulk deleted ${messages.size} messages`))
  .catch(console.error);
  for (let step = 0; step < 5; step++) 
  channel.send("This channel is closed... Please dont type in it!")
  }}







})
client.on('guildMemberAdd', member => {
    const channel = client.channels.cache.get(censored');
    channel.send('A non-whitelisted member has tried to join')
  if(member.id == "censored") {
}else {
  client.users.cache.get(member.id).send('You are not whitelisted');
  member.kick()
}
});



client.login("censored")

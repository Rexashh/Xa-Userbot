# @JustRex
#Xa-Userbot
#Special Ramadhan

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, Xa_cmd


@Xa_cmd(pattern="puasa1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamualaikum kak ,Masih Semangat kan Puasanya?**")


@Xa_cmd(pattern="puasa2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ngabuburit yok!**")


@Xa_cmd(pattern="puasa3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Maap lagi ga mau gibah gua lagi puasa!**")
    
    
@Xa_cmd(pattern="puasa4(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Ganteng Doang, Puasa Kagak!!!**")
    
    
@Xa_cmd(pattern="puasa5(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event,**Cieeeee Ga Puasa**")
    

@Xa_cmd(pattern="puasa6(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event,**Bangga lo ga puasa? Gua sih Malu!**")


@Xa_cmd(pattern="takjil1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Info Takjil Gratis, yang ada koleknya!**")


@Xa_cmd(pattern="takjil2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Ada yang mau ikut gua nyari takjil ga??**")
    

@Xa_cmd(pattern="takjil3(?: |$)(.*)")
async def_(event):
    await edit_or_reply(event, "**Gopudin makanan dong, Buat Buka :(**")
    


@Xa_cmd(pattern="ngaji1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Daripada War mending ngaji kak**")


@Xa_cmd(pattern="ngaji2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Gibah mulu lu, ngaji lah!!**")


@Xa_cmd(pattern="sabar1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Sabar Aja, Kan lagi Puasa**")


@Xa_cmd(pattern="sabar2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Untung Lagi puasa jadinya gua Sabar**")


@Xa_cmd(pattern="setan1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Gua ga gampang Kehasut Setan Kek lu**")


@Xa_cmd(pattern="setan2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Setan Kok Ngehasut Setan?**")


@Xa_cmd(pattern="setan3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CIE SETAN LAGI NGEGODA**")


@Xa_cmd(pattern="sedekah1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Ga ada yang niat sedekah Ke Gua nih?**")


@Xa_cmd(pattern="sedekah2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Bagi duit dong buat beli baju Lebaran :)**")


@Xa_cmd(pattern="s1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Jum'atan dulu ah.... Mau Farming Sendal**")


@Xa_cmd(pattern="s2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Sholat ah Biar Ganteng**")


@Xa_cmd(pattern="s3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "***Puasa doang, Sholat Kagak!!**")


@Xa_cmd(pattern="warteg1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Info Warteg yang buka dong gaes!**")


@Xa_cmd(pattern="warteg2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**WARTEG KUY!!**")


@Xa_cmd(pattern="warteg3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Bentar, Gua mau Ke Warteg dulu, Laper bgt anjg!**")

    
@Xa_cmd(pattern="sahur1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Ga semangat Puasanya, gara gara Ga dibangunin sahur sama ayang**")
    
   
@Xa_cmd(pattern="sahur2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SAHUR WOIII SAHURRRR!!**")  
    
    
@Xa_cmd(pattern="buka(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Selamat Berbuka...**")
   
   
@Xa_cmd(pattern="magrib(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Cieeee Lagi nungguin Adzan Magrib wkwkw**")
    
    
@Xa_cmd(pattern="bukber(?: |$)(.*)")
async def _(event):
    await edit_or_rey(event, "**Ga ada niatan Bukber ni GC?**")
    

@Xa_cmd(pattern="bukber2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Gausah sok ngajakin Bukber kalo ujung ujungnya cuma Wacana!**")
    
    
@Xa_cmd(pattern="bukber3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BUKBER = WACANA**")
    

@Xa_cmd(pattern="bukber4(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BUKBER KUY!!!!**")
    
    
@Xa_cmd(pattern="puasasad(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Mau Bukber sama Ayang tapi ga punya**")

CMD_HELP.update(
    {
        "ramadhan": f"**Plugin : **`ramadhan`\
        \n\n      **Perintah** : {cmd}puasa1\
        \n**⌬Fungsi : **Nanya Semangat ga puasanya ke orang, cobain aja jing\
        \n\n     **Perintah** : {cmd}puasa2\
        \n**⌬Fungsi : **Ngajak Ngabuburit 
        \n\n    **Perintah** : {cmd}puasa3\
        \n**⌬Fungsi : **Ga mau Gibah
        \n\n    **Perintah** : {cmd}puasa4\
        \n**⌬Fungsi : **Ganteng doang, Puasa kaga!
        \n\n    **Perintah** : {cmd}puasa5\
        \n**⌬Fungsi : **Cie Ga puasa\
        \n\n    **Perintah** : {cmd}puasa6\
        \n**⌬Fungsi : **Bangga lu ga puasa?\
        \n\n    **Perintah** : {cmd}takjil1\
        \n**⌬Fungsi : **Info Takjil Gratis\
        \n\n    **Perintah** : {cmd}takjil2\
        \n**⌬Fungsi : **ngajak nyari takjil\
        \n\n    **Perintah** : {cmd}takjil3\
        \n**⌬Fungsi : **gopudin cok\
        \n\n    **Perintah** : {cmd}ngaji1\
        \n**⌬Fungsi : **gausah war mending ngaji\
        \n\n    **Perintah** : {cmd}ngaji2\
        \n**⌬Fungsi : **gapengen gibah\
        \n\n    **Perintah** : {cmd}sabar1\
        \n**⌬Fungsi : **sabar lu kan lagi puasa\
        \n\n    **Perintah** : {cmd}sabar2\
        \n**⌬Fungsi : **cobain ajalah\
        \n\n    **Perintah** : {cmd}setan1\
        \n**⌬Fungsi : **ngatain orang setan\
        \n\n    **Perintah** : {cmd}setan2\
        \n**⌬Fungsi : **setan ngehasut setan\
        \n\n    **Perintah** : {cmd}setan3\
        \n**⌬Fungsi : **cie lagi ngehasut\
        \n\n    **Perintah** : {cmd}sedekah1\
        \n**⌬Fungsi : **cobain aja males ngetik\
        \n\n    **Perintah** : {cmd}sedekah2\
        \n**⌬Fungsi : **sedekah baju lebaran\
        \n\n    **Perintah** : {cmd}s1\
        \n**⌬Fungsi : **sholat\
        \n\n    **Perintah** : {cmd}s2\
        \n**⌬Fungsi : **sholat\
        \n\n    **Perintah** : {cmd}s3\
        \n**⌬Fungsi : **sholat !\
        \n\n    **Perintah** : {cmd}warteg1\
        \n**⌬Fungsi : **Info Warteg yang buka\
        \n\n    **Perintah** : {cmd}warteg2\
        \n**⌬Fungsi : **ngajak kewarteg\
        \n\n    **Perintah** : {cmd}warteg3\
        \n**⌬Fungsi : **Izin kewarteg\
        \n\n    **Perintah** : {cmd}sahur1\
        \n**⌬Fungsi : **Ga disemangatin ayang sahurnya\
        \n\n    **Perintah** : {cmd}sahur2\
        \n**⌬Fungsi : **Sahur woi!!\
        \n\n    **Perintah** : {cmd}buka\
        \n**⌬Fungsi : **selamat berbuka\
        \n\n    **Perintah** : {cmd}magrib\
        \n**⌬Fungsi : **ciee nunggu adzan akunya kapan? :(\
        \n\n    **Perintah** : {cmd}bukber1\
        \n**⌬Fungsi : **ngajak bukber gc\
        \n\n    **Perintah** : {cmd}bukber2\
        \n**⌬Fungsi : **Buat orang yg ngajak bukber tapi cuma wacana\
        \n\n    **Perintah** : {cmd}bukber3\
        \n**⌬Fungsi : **Bukber=Wacana\
        \n\n    **Perintah** : {cmd}bukber4\
        \n**⌬Fungsi : **Ngajar Bukber\
        \n\n    **Perintah** : {cmd}puasasad\
        \n**⌬Fungsi : **cobain aja ya\
    "
    })

function validateAttendance()
{
    console.log("In JS method")
    id=1
    while(id<=40)
    {
        inpObject = document.getElementsByName(Integer.toString(id))
        if(inpObject.checked==false)
        {
           msg='All student attendence must be selected';
           document.getElementById('msg').innerHTML=msg;
           break
        }
        id+=1
    }
    if(id==40){

    }
}
function display(data)
{
    input = document.getElementById('inputElement');        // Input Field
    if(data=='=')
        input.value = eval(input.value);
    else if(data=='AC')  
      input.value = 0;                              // Initialize input field with 0
    else if((data=='00' || data=='0') && input.value==0)           // If input field contain zero then after pressing 00 also it just remain same as 0
      input.value=0;
    else if(data=='DEL')
        input.value=input.value.substring(0, input.value.length-1);      // removes last char & return string without last char
    else
    {
         if(input.value=='0')
            input.value='';
         input.value = input.value+data;
    }
    // else if(data>=0 && data<=9)
    //    input.value= input.value*10+data;            // String type data is taken
    // else if((input.value[input.value.length-1]>=0 && input.value[input.value.length-1]<=9) &&  (data=='%' || data=='+' || data=='-' || data=='*' || data=='/' || data=='=' || data=='.'))
    //    input.value = input.value+data;             // If last char is operator & still user trying to press operator it doesn't take input   
}

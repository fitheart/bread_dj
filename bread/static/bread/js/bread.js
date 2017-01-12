/**
 * Created by Admin on 10/5/2016.
 */


function jk_send_contact() {
    alert('12121');
    console.log('jk_send_contact');
    var username = document.getElementById("inputUsername").value;
    var subject = document.getElementById("inputSubject").value;
    console.log('username:' + username + 'email:' + subject );
    // $.ajax(
    //     {
    //              type:"POST",
    //              url:"/contact/",
    //              dataType:'json',
    //              data: {
    //                     'username': username ,
    //                     'subject': subject,
    //                     },
    //              success: function(response){
    //                    console.log('jk_send_contact ===> success');
    //                     console.log(response);
    //                     console.log('END jk_send_contact');
    //              },
    //             error: function (err) {
    //                 console.log('jk_send_contact ===> failed');
    //             }
    // }
    // );
    // jQuery.ajax({
    //              type:"POST",
    //              url:"/contact/",
    //              dataType:'json',
    //              data: {
    //                     username ,
    //                     subject,
    //                     },
    //              success: function(response){
    //                    console.log('jk_send_contact ===> success');
    //                     console.log(response);
    //                     console.log('END jk_send_contact');
    //              },
    //             error: function (err) {
    //                 console.log('jk_send_contact ===> failed');
    //             }
    // });

}



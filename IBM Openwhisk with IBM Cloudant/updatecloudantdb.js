function main(params){
   return new Promise(function(resolve,reject){
       console.log(params.firstname);
       console.log(params.lastname);

       if(!params.name){
           console.error('name parameter not set')
           reject({
               'error':'name of parmeter not set'
            });
           return;
       }
       else{
            var message=+params.firstname + ' '+params.lastname + ' was added';
            console.log(message);
            resolve({
                change:message
            });
            return;
       }
   });
}
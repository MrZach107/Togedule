function postData(url, data) {
  // Default options are marked with *
  return fetch(url, {
      body: JSON.stringify(data), // must match 'Content-Type' header
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, same-origin, *omit
      headers: {
          'user-agent': 'Example',
          'content-type': 'application/json'
      },
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, cors, *same-origin
      redirect: 'follow', // manual, *follow, error
      referrer: 'no-referrer', // *client, no-referrer
  })
      .then(response => response.json()) // 輸出成 json
}

function submit(){
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const id = {
    email,
    password
  }

  postData("http://0.0.0.0:3000/id",id)
  .then(id=>{
    console.log(id);
  })

}


/*
id.addEvenListener('submit',()=> {
  let user = email.value
  
  event.preventDefault() // 新增此行
  password.innerHTML = `<h3 class="display-3">Hi, ${user}</h3>`
}
*/

)

<template>
  <section class="login_container">
      <div class="login_panel">
        <input class="form-element" v-model="username" placeholder="username" type="username" >
        <input class="form-element" v-model="password" type="password"   placeholder="password"/>
        <button v-on:click="login" class="form-element">Login</button>
      </div>

      <h1>{{message}}</h1>
    </section>
</template>

<script>
import axios from 'axios'


export default {
  name: "Login",
  data() {
    return {
      message:"",
      username: "",
      password: "" 
    };
  },
  beforeCreate: function () {
    if (this.$session.exists()) {
      this.$router.push({ name: "user-loans", params: { user: this.$session.get('user')}})
    }
  },
  methods: {
    login() {
      console.log(this.username);
      var  id_user="!";
      
      axios.post('http://localhost:8000/api-token-auth/',
      {username:this.username, password:this.password} ).then((res)=>{
         if (res.status === 200) {
            console.log(res.data);
            this.message = res.data.token;
            let url="http://127.0.0.1:8000/users/?search="+ this.password;
            axios.get(url).then((response)=>{
               console.log(response.data);
               id_user= response.data[0].id;
               id_user.toString();
               console.log(id_user);
               this.$session.start();
               this.$session.set('user', id_user);
               console.log(this.$session.get('user'));
               this.$router.push({ name: "user-loans", params: { user: id_user}});
             })
          }
      }).catch(()=> {
        this.message="qualcosa è andato storto";
          
        })
    }
  }
};
</script>

<style scoped>
.login_container {
  padding-top: 2.75 rem;  
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.login_panel {
  max-width: 50%;
  padding: 2.75rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #fff;
  border-radius: .25rem;
  box-shadow: 1px 1px 5px 0px rgba(0,0,0,0.75);
}
.form-element {
    display: block;
    width: 100%;
    height: calc(2.25rem + 2px);
    padding: .3rem .7rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #297aca;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    margin-bottom: 1rem!important;
}
</style>
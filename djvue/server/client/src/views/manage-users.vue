<template>
  <div class="container-fluid">
    <div class="row" >
      <div class="col-sm-12">
        <h2>Users  </h2>
      </div>
    </div>
    <div class="form-row" >
      <div class="col-lg-6 mb-2 flex-column" v-for="user in users" :key="user.id">
        <div class="card h-100">
          <div class="card-header d-flex">
            <h4
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center"
              :title="user.username"
            >{{user.username}} </h4>
            <button
              class="btn btn-lg btn-link flex-grow-0 flex-shrink-0"
              @click="askToDelete(user)"
            >Elimina user</button>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-lg-6">
                <h5 class="card-title">Indirizzo</h5>
                {{user.email}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'ManageUsers',
    data() {
    return {
      users:null,
      url:'',
      username:'',
      email:'',
    };
  },
  mounted(){
    this.getAll();
  },
  methods: {
    getAll(){
      axios.get('http://localhost:8000/users').then((res)=>{
          this.users=res.data;
          this.url='';
          this.username='';
          this.email='';
      })
    },    
    getOne(user){
      this.url=user.id;
      this.username=user.username;
      this.email=user.email;
    },
    askToDelete(url){
      axios.delete(url,{auth:{
            username:'admin',
            password: 'admin'
          }})
      .then(()=>{
          this.getAll();
        })
    } 
  }
};
</script>
<style scoped lang="scss">
.card {
  min-height: 150px;
}
</style>

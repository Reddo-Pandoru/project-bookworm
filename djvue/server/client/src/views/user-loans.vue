<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12" >
        <h2>Libri presi in prestito </h2>
      </div>
    </div>
    <div class="form-row">
      <div class="col-lg-6 mb-2 flex-column" v-for=" (loan, index) in loans" :key="loan.url" >
        <div class="card h-100">
          {{getbook(loan.volume_id, index)}}
          <div class="card-header d-flex">
            <h4 
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center">
             {{  book[0] }} </h4>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-lg-6">
                <label>data di restituzione</label>
                {{loan.return_date.substring(0, 10)}}
              </div>
              <div class="col-lg-6">
                <label></label>
                
              </div>
              <div v-if="loan.prolungato">
                <label>prolungazione del prestito già avvenuta</label>
              </div>
              <div v-else>
                <label>possibilità di prolungare il prestito</label>
                <button
                  class="btn btn-lg btn-link flex-grow-0 flex-shrink-0" v-on:click="getone(loan)">prolunga</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <img  v-bind:src="'http://localhost:8000/media/utente_'+this.$route.params.user+'.jpg'" alt="" width="200" height="200">
    <button v-on:click="logout" class="btn btn-lg btn-primary mr-2">logout</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ManageBooks',
  
  data() {
    return {
      book:[''],
      loans:null,
      prolungato:null,
      url:'',
      return_date :'',
      borrow_date :'',
      user :'',
      volume:''
    };
  },
  mounted(){
    this.getAll();
  },
  methods: {
    getAll(){
      let url="http://127.0.0.1:8000/loans/?user="+ this.$route.params.user;
      console.log(this.$route.params.user);
      axios.get(url).then((res)=>{
          console.log("fase finale");
          this.loans=res.data;
          console.log(res.data);



        }).catch(()=> {
        this.$router.push({ name: "manageUsers"})
          
        })


     },
    getbook(volume_id, index){
      let name=null;
      let url= 'http://127.0.0.1:8000/volumes/?search='+ volume_id;
      axios.get(url).then((res)=>{
        console.log(res.data);
        name=res.data[0].book;
        this.book[index]=name;
        console.log(this.book);
      })
    },
    getone(loan){
      this.url=loan.url;
      this.return_date=loan.return_date;
      this.borrow_date=loan.borrow_date;
      this.user=loan.user;
      this.volume=loan.volume;
      this.extend();
    },
    extend(){
      axios.put(this.url, {
        prolungato:true,
        url:this.url,
        return_date:this.return_date,
        borrow_date:this.borrow_date,
        user:this.user,
        volume:this.volume},
        {auth:{username:'admin', password: 'admin'}}
      ).then(()=>{
        this.getAll();
      })
    },
    logout: function () {
      this.$session.destroy()
      this.$router.push('/')
    }
  }
}
</script>
<style scoped lang="scss">
.card {
  min-height: 150px;
}
</style>
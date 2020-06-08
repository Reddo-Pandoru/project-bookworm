<template>
  <div class="row">
  <div class="col-lg-6" >
    <input class="form-control mt-2"  v-model="url" hidden >
    <input class="form-control mt-2" type="text" v-model="first_name" placeholder="first_name" required>
    <input class="form-control mt-2" type="text" v-model="last_name" placeholder="last_name" required>
    <input class="form-control mt-2" type="date" id="start" name="trip-start"
       min="1000-01-01" v-model="birth_date" placeholder="birth date" required>
    <input class="form-control mt-2" type="date" id="start" name="trip-start"
       min="1000-01-01" v-model="death_date" placeholder="birth death" >
    <select v-model="name">
   <option v-for="country in countries" v-bind:key="country.url" v-bind:value="country.id" >
    {{ country.name }}
  </option>
</select>   
<span>Selected: {{ name }}</span>
   <!-- <input class="form-control mt-2" type="text" v-model="first_name" placeholder="first_name">
-->
    
    <button @click="postauthor" class="btn bn-sm btn-success mt-2">save</button>

   </div>
  <div class="col-lg-6" > 
    <table class="table">
      <thead>
        <th>url</th>
        <th>nome</th>
        <th>cognome</th>
        <th>data di nascita</th>
        <th>data di morte</th>
        <th>nazione</th>
      </thead>
      <tbody>
        <tr v-for="author in authors" v-bind:key="author.url">
          <td>{{author.url}}</td>
          <td>{{author.first_name}}</td>
           <td>{{author.last_name}}</td>
          <td>{{author.birth_date}}</td>
           <td>{{author.death_date}}</td>
          <td>{{author.country_id}}</td>
          <td>
            <button @click="getOne(author)" class="btn bn-sm btn-success"><i class="fa fa-pencil" aria-hidden="true"></i></button>
          </td>
           <td>
            <button @click="deleteOne(author.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
          </td>
        </tr>
      </tbody>

    </table>
  </div>
 
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ManageAuthors',
  data(){
    return{
      authors:null,
      countries:null,
      url:'',
      first_name:'',
      last_name:'',
      birth_date:'',
      death_date:'',
      note:'',
      country_id:'',
      name:''



    }
  },
  mounted(){
    this.getAll();
    this.getCountryName();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/authors').then((res)=>{
          this.authors=res.data;
          this.url='';
          this.first_name='';
          this.last_name='';
          this.birth_date='';
          this.death_date='';
          this.note='';
          this.country_id='';


      })},
      getCountryName(){
      axios.get('http://localhost:8000/countries').then((res)=>{
         this.countries=res.data;
         this.name='';
         console.log(res.data);

      
      })  
    },
    getOne(author){
      this.url=author.url;
      this.first_name=author.first_name;
    },
    deleteOne(url){
      axios.delete(url,{auth:{
            username:'admin',
            password: 'admin'
          }})
      .then(()=>{
          this.getAll();
        })
    },
    postauthor(){
      if(this.url==''){
        axios.post('http://localhost:8000/authors/',
        { first_name:this.first_name,
          last_name:this.last_name,
          birth_date:this.birth_date,
          death_date:this.death_date,
          note:'tentativo',
          country_id:1},
           {auth:{
              username:'admin',
              password: 'admin'
          }},
          ).then(()=>{
            this.getAll();
        })}
      else{
         axios.put(this.url,
        {first_name:this.first_name,
          last_name:this.last_name,
          birth_date:this.birth_date,
          death_date:this.death_date,
          note:'tentativo'
          ,country_id:1},
          {auth:{
            username:'admin',
            password: 'admin'
          }}).then(()=>{
            this.getAll();
        })
      }  
        
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

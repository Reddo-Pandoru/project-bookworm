<template>
  <div class="row">
  <div class="col-lg-6" >
    <input class="form-control mt-2" type="hidden" v-model="url" >
    <input class="form-control mt-2" type="text" v-model="type" placeholder="type">
    
    <button @click="postgenre" class="btn bn-sm btn-success mt-2">save</button>

   </div>
  <div class="col-lg-6" > 
    <table class="table">
      <thead>
        <th>url</th>
        <th>type</th>
        <th>Edit</th>
        <th>Delete</th>
      </thead>
      <tbody>
        <tr v-for="genre in genres" v-bind:key="genre.url">
          <td>{{genre.url}}</td>
          <td>{{genre.type}}</td>
          <td>
            <button @click="getOne(genre)" class="btn bn-sm btn-success"><i class="fa fa-pencil" aria-hidden="true"></i></button>
          </td>
           <td>
            <button @click="deleteOne(genre.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
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
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      genres:null,
      url:'',
      type:'',



    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/genres').then((res)=>{
          this.genres=res.data;
          this.url='';
          this.type='';
      })
    },
    getOne(genre){
      this.url=genre.url;
      this.type=genre.type;
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
    postgenre(){
      if(this.url==''){
        axios.post('http://localhost:8000/genres/',
        {type:this.type}, {auth:{
            username:'admin',
            password: 'admin'
          }},
          ).then(()=>{
            this.getAll();
        })}
      else{
         axios.put(this.url,
        {type:this.type},
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
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

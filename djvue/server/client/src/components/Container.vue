<template>
  <div class="row">
  <div class="col-lg-6" >
    <input class="form-control mt-2" type="hidden" v-model="url" >
    <input class="form-control mt-2" type="text" v-model="title" placeholder="title">
    <input class="form-control mt-2" type="text" v-model="body" placeholder="body" id="">
    <button @click="postBook" class="btn bn-sm btn-success mt-2">save</button>

   </div>
  <div class="col-lg-6" > 
    <table class="table">
      <thead>
        <th>url</th>
        <th>Title</th>
        <th>Body</th>
        <th>Edit</th>
        <th>Delete</th>
      </thead>
      <tbody>
        <tr v-for="book in books" v-bind:key="book.url">
          <td>{{book.url}}</td>
          <td>{{book.book_name}}</td>
          <td>{{book.body}}</td>
          <td>
            <button @click="getOne(book)" class="btn bn-sm btn-success"><i class="fa fa-pencil" aria-hidden="true"></i></button>
          </td>
           <td>
            <button @click="deleteOne(book.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
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
      books:null,
      url:'',
      title:'',
      body:'',



    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/books').then((res)=>{
          this.books=res.data;
          this.url='';
          this.title='';
          this.body='';
      })
    },
    getOne(book){
      this.url=book.id;
      this.title=book.title;
      this.body=book.body;
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
    postBook(){
      if(this.url==''){
        axios.post('http://localhost:8000/books/',
        {title:this.title,body:this.body}, {auth:{
            username:'admin',
            password: 'admin'
          }},
          ).then(()=>{
            this.getAll();
        })}
      else{
         axios.put(this.url,
        {title:this.title,body:this.body},
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

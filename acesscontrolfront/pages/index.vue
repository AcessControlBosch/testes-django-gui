<template>

  <div class="container">

    <Header />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="edv" class="label-form">EDV:</label>
          <input type="text" placeholder="Digite o EDV..." id="edv" class="input-form" v-model="user.username"/>

          <label for="senha" class="label-form">Senha:</label>
          <input type="password" placeholder="Digite a senha..." id="senha" class="input-form" v-model="user.password"/>


          <div class="align-items-center">

            <button class="btn-logar" v-on:click="makeLogin()">Logar</button>

          </div>

          <div class="align-items-center">

            <button class="btn-redirect" v-on:click="$router.push('/screen_criarConta')">Não possue conta? Clique aqui</button>

          </div>
        
        </div>
    
    </div>

  </div>

</template>

<script>

export default {
  
  name: 'IndexPage',

  data(){

    return{

      dataUser: [],
      user:{
        username: '',
        password: '',
      }

    }

  },

  methods: {

    //funcao para setar usuário
    setUser: async function(){

      console.log(this.dataUser);

      let increment = 0;

      for(increment; increment < this.dataUser.length; increment++){

        if(this.dataUser[increment].EDV == this.user.username){

          this.$store.dispatch("SET_USER", this.dataUser[increment]);
          break;
          
        }

      }

    },

    //funcao para buscar usuarios
    searchUser: async function(){

        this.$axios.get(this.$store.state.BASE_URL + "/users").then((response) =>{

          //console.log("Encontrou os dados")

          this.dataUser = response.data;

          this.setUser();
    
        }).catch((error) => {
          console.log("Vish, deu ruim!");
          console.log(error);
        });

        
    },

    //função para fazer login
    makeLogin: async function(){

      if(this.user.username && this.user.password){

        this.$auth.loginWith(
          
          "local", {data: this.user})
          .then((response) => {
            this.searchUser();

            console.log("response",response)
            console.log("Usuário Logado")

            

        }).catch((response) =>{

          console.log('response',response)

        })

      } else {
        alert("Preencha todos os campos")
      }
    }
  },

}

</script>

<style lang="scss" scoped>

   @import "@/layouts/_normal_pages/Index.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";

</style>

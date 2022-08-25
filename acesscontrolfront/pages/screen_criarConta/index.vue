<template>

  <div class="container">

    <HeaderWithHome />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="nome" class="label-form">Nome:</label>
          <input type="text" placeholder="Digite o seu nome..." id="nome" class="input-form" v-model="dataUser.name"/>

          <label for="edv" class="label-form">EDV:</label>
          <input type="text" placeholder="Digite o seu EDV..." id="edv" class="input-form" v-model="dataUser.edv"/>

          <label for="edv" class="label-form">Área:</label>
          <Dropdown v-model="selectedArea" :options="this.dataArea" optionLabel="name" placeholder="Selecione a área..." />

          <div class="align-items-center">

            <button class="btn-send-approved" v-on:click="sendData()">Enviar</button>

          </div>
        
        </div>
    
    </div>

  </div>

</template>

<script>
export default {
  name: 'screen_criarConta',
  data() {
	return {
    selectedArea: 0,
    dataArea: [],
    dataUser:{
        name:'',
        edv: '',
        area: 0,
    }
  }
},
  created(){
    console.log()
    this.$axios.get(this.$store.state.BASE_URL + "/areas").then((response) =>{

      this.dataArea = response.data;
    
    }).catch((error) => {
        console.log("Vish, deu ruim!");
        console.log(error);
    });
  },
  methods:{
    
    sendData: async function(){

      let body = [{
          name: this.dataUser.name,
          EDV: this.dataUser.edv,
          idAreaFK: this.selectedArea.id
      }];

      console.log(body)

        if(body.name != "" && body.EDV != "" && body.idAreaFK != 0){

          console.log("entrou")

          this.$axios.post(this.$store.state.BASE_URL + "/requestLogins/", body).then((response) => {
            alert("Envio com sucesso! Sua requisição sera avaliada por um administrador!");
          }).catch((error) => {
            alert("Atenção, usuário não cadastrado!");
            console.log(error);
          });
        } else {
          alert("Preencha todos os campos!")
        }
 
    }
  }
}
</script>

<style lang="scss" scoped>
 
   @import "@/layouts/_normal_pages/Screen_CriarConta.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";
</style>
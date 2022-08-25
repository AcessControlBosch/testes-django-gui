<template>

    <div class="container">
    
        <Header />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div> 

            <div class="row-inferior">

                <div class="card-info">
                
                    <p class="card-title">Segurança</p>
                    <p class="card-subject">Requisitos de Segurança de acordo com o equipamento:​</p>


                </div> 

                <div class="formulario">

                    <div class="line-question" v-for="(question, id) in allQuestions" :key="id">

                        <input type="checkbox" class="checkbox" v-bind:value="id" v-model="valueCheckBox" v-bind:id="idQuestion[id] - 1"/>
                        <label class="p-question" for="um">{{idQuestion[id]}} - {{question.question}}</label>
                        
                    </div>
                </div>


                <div class="align-items-center">
            
                    <button class="btn btn-sucess" v-on:click="verifyQuestions()">Continuar</button>
                    <button class="btn btn-alert" v-on:click="$router.push('/screen_home')">Cancelar</button>
            
                </div>
            
            </div>

        </div>

        <div v-if="showModal">
        
            <ModalOrdemChamadoSeguranca />
        
        </div>
    
    </div>

</template>

<script>

export default {

    name: 'screen_cvSeguranca',

    data(){

        return{

            allQuestions: [],
            responseQuestions: [],
            valueCheckBox: [],
            idQuestion:[],
            path: '',
            showModal: this.$store.state.modalSecurity,    
        }

    },

    created(){

        console.log(this.$store.state.idmachine);

        this.path = this.$store.state.BASE_URL + '/greenbooks/' + this.$store.state.idmachine + '/2'

        console.log(this.path);

        this.$axios.get(this.path).then((response) => {

            //console.log('oi created')

            this.allQuestions = response.data;

            //console.log(this.allQuestions)

            let i = 0;

            for(i; i < this.allQuestions.length; i++){

                this.responseQuestions.push(this.allQuestions[i].question);
                this.idQuestion.push(i+1);

            }

            //console.log('this.idQuestion',this.idQuestion)

        }).catch((error) => {

            console.log(error)

        })

    },

    methods: {

        showModalBar: function(){

            this.showModal = this.$store.state.modalSecurity;

        },

        verifyQuestions: function(){

            console.log(this.$store.state.machine)

            let qNotMarked  = [];
            let increment = 0;

            for(increment; increment < this.allQuestions.length; increment++){

                var checkedValue = document.getElementById(increment).checked;

                if(checkedValue == false){
                    qNotMarked.push(increment + 1);
                }

            }

            this.$store.dispatch("SET_QNOTMARKEDSECURITY", qNotMarked);

            if(this.$store.state.qNotMarkedSecurity.length > 0){

                this.$store.dispatch("SET_MODALSECURITY", true);
                this.showModalBar();
            
            } else {

                this.$router.push('/screen_cvMeioAmbiente');

            }

        }

    },

}

</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_CvSeguranca.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>
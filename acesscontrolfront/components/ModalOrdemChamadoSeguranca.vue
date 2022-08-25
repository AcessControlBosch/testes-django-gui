<template>

    <div>

        <Dialog 
            class="modalImg"
            :visible.sync="showDialogV"
            :dismissableMask="true"
            :closeOnEscape="true"
                    
            :style="{width: '300px', backgroundColor: 'yellow'}"        
            >      
            <p class="titleModalcss">Atenção, checklist incompleto!</p> 
            <p class="messageModalcss">Alguns itens não estão em conformidade: {{ this.$store.state.qNotMarkedSecurity }}</p>
            

            <p>Abrir ordem de chamado:</p>

            <div class="aling-itens-center">

                <button class="btn-success" v-on:click="routerOrdem()"><p>Sim</p></button>
                <button class="btn-warming" v-on:click="routerSecurity()"><p>Não</p></button>

            </div>

        </Dialog>
    
    </div>

</template>


<script>
export default {
    
    name: 'ModalOrdemChamadoSeguranca',

    data() {
        return {
            showDialogV: this.$store.state.modalSecurity,
        }
    },

    methods:{
        
        showModal(){
                this.showDialogV = true;
        },

        
        routerOrdem: function(){
            this.$router.push("/screen_ordemManutencao")
        },

        routerSecurity: function(){
            this.$store.dispatch("SET_MODALSECURITY", false);
            this.showDialogV = this.$store.state.modalSecurity;
            this.$router.push("/screen_home")
        }
        

    }
}
</script>

<style lang="scss" scoped>

    @import "@/layouts/_scss_components/ModalOrdemChamadoSeguranca.scss";
    
</style>
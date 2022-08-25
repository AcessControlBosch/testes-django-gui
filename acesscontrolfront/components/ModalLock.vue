<template>

    <div>

        <Dialog 
            class="modalImg"
            :visible.sync="showDialogV"
            :dismissableMask="true"
            :closeOnEscape="true"
                    
            :style="{width: '300px', backgroundColor: 'yellow'}"        
            >      
            <p class="titleModalcss">Máquina Bloqueada!</p> 
            <p class="messageModalcss">Seu chamado de ordem de manutenção foi aberto, aguarde a análise do responsável pela máquina!</p>
            <i  class="pi pi-lock"></i>
        </Dialog>
        </div>

</template>


<script>


export default {
    name: 'ModalLock',
    data() {
        return {
            showDialogV: true,
            
        }
    },
    methods:{
        showModal(){
                this.showDialogV = true;
            }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/layouts/_scss_components/ModalLock.scss";
</style>
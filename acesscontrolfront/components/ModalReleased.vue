<template>

    <div>

        <Dialog 
            class="modalImg"
            :visible.sync="showDialogV"
            :dismissableMask="true"
            :closeOnEscape="true"
                    
            :style="{width: '300px', backgroundColor: 'yellow'}"        
            >      
            <p class="titleModalcss">Máquina Liberada!</p> 
            <p class="messageModalcss">A máquina está em conformidade.</p>
            <i  class="pi pi-lock-open"></i>
        </Dialog>
    
    </div>

</template>


<script>
export default {
    
    name: 'ModalReleased',

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

    @import "@/layouts/_scss_components/ModalReleased.scss";
    
</style>
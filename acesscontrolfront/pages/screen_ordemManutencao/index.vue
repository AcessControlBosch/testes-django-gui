<template>
    <div class="container">

        <Header />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div>

            <div class="row-inferior">
            
                <div class="card-info">
                    <div>
                        <p class="card-title">Abertura de Ordem de Manutenção</p>
                    </div>
                </div>

                <div class="conteudo">
                    <p>Descreva abaixo a inconformidade encontrada:</p>

                    <Textarea :autoResize="true" rows="15" cols="10" />
                </div>

                <div class="align-items-center">
            
                        <button class="btn btn-sucess" v-on:click="showModal()">Enviar</button>

                        <div v-if="showDialogV" >
                            <ModalLock/>
                        </div>
            
                    </div>  
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    name: 'screen_ordemManutencao',
    data(){
        return {
            showDialogV: false,
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
    @import "@/layouts/_normal_pages/Screen_OrdemManut.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";
</style>
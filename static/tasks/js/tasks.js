new Vue(
    {
        el: '#tasks',
        data: {
            tasks: []
        },
        created: function() {
            const vm = this;
            axios.get('/tasks/api/tasks/')
                .then(function(response) {
                    // console.log(response.data)
                    vm.tasks = response.data
                })
        }
    }
)
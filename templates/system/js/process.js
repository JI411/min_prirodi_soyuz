document.addEventListener("DOMContentLoaded", ()=>{
	PROCESS.init()
});

const PROCESS = {
	files: false,
	image_current: 0,
	images_sum: 0,


	init() {
		DAN.$('mainpage_submit').onclick = PROCESS.files_upload
		PROCESS.images()
	},


	// Загрузка изображений
	images(){
		DAN.$('mainpage_files').onchange = function(){
			PROCESS.files = this.files

			if (!PROCESS.files) {
				alert('Не выбрано ни одного изображения')
				return;
			}

			for (var i = 0; i < PROCESS.files.length; i++) {
				if (!PROCESS.files[i].type.match(/image.*/)) {
					alert('Данный формат файла не поддерживается: ' + PROCESS.files[i].name)
					return;
				}
				if (PROCESS.files[i].size > 4096000) {
					alert('Размер изображения ' + PROCESS.files[i].name + ' ' + PROCESS.files[i].size + ' более 4 Мб.');
					return false;
				}
			}

			PROCESS.images_sum = PROCESS.files.length
			let progress_bar = 	'<h2>Загрузка <span id="dan_modal_current">0</span> из <span id="dan_modal_sum">' + PROCESS.files.length + '</span></h2>' +
								'<div><progress id="dan_modal_progress" max="' + PROCESS.files.length + '" value="0"></progress></div>' +
								'<div><span id="dan_modal_current_filename"></span></div>'

			DAN.modal.add(progress_bar, 450)
			PROCESS.images_loading()
		}
	},


	// Пошаговая загрузка файлов
	images_loading() {
		let form = new FormData()
		form.append('image', PROCESS.files[PROCESS.image_current])

		// Начинаем загрузку с 0 индекса
		DAN.ajax('/system/image_upload_ajax', form, (data) => {
			PROCESS.image_current++
			DAN.$('dan_modal_current').innerHTML = PROCESS.image_current
			DAN.$('dan_modal_progress').value = PROCESS.image_current

			if (PROCESS.image_current >= PROCESS.images_sum) {
				DAN.$('dan_modal_current_filename').innerHTML = 'Загрузка завершена'
				PROCESS.images_processing()
				return
			} else {
				DAN.$('dan_modal_current_filename').innerHTML = PROCESS.files[PROCESS.image_current]['name']
			}

			console.log(data.name)
			PROCESS.images_loading()
		})
	},


	// Пошаговая обработка изображений
	images_processing() {
		let form = new FormData()
		// form.append('image', PROCESS.files[PROCESS.image_current])
		DAN.modal.add('ПРИСТУПАЕМ К ОБРАБОТКЕ ИЗОБРАЖЕНИЙ')

		DAN.ajax('/system/image_processing_ajax', form, (data) => {
			DAN.modal.add('ОБРАБОТКА ЗАВЕРШЕНА!')
			document.location.href = '/system/result'
		})
	}
}
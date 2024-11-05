stamp=$(date "+%Y-%m-%d_%H-%M-%S")

log_dir="outputs/" # TODO
prompt="a wooden bear"
scene_id="bear/bear_1"
python scripts/train_texture.py --config config/template.yaml --stamp $stamp --log_dir $log_dir --prompt "$prompt" --scene_id "$scene_id"
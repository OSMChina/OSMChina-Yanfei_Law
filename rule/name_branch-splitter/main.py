import argparse
import re

from keqing_my_waifu.pyosm import PyOsm, BaseOsmModel


def main(args: argparse.Namespace):
    pyosm = PyOsm()
    try:
        pyosm.from_file(args.src)
    except FileNotFoundError:
        print('文件%s不存在' % args.src)

    for node in pyosm.node_dict.values():
        process(node)
    for way in pyosm.way_dict.values():
        process(way)
    for relation in pyosm.relation_dict.values():
        process(relation)
    pyosm.write(args.dst)
    if args.pause:
        input('\n按任意键退出…')


def process(model: BaseOsmModel):
    if 'amenity' not in model.tags or model.tags['amenity'] != 'bank':
        return
    if 'process_with_robot' in model.tags and model.tags['process_with_robot'] == 'no':
        return
    name = model.tags['name']
    name = re.sub('[\\[\\]{}()（）「」【】〔〕［］]', '', name)
    if re.search('银行.*[分支]行$', name):
        bank_end_index = name.index('银行') + 2  # 截取'**分行'
        branch = name[bank_end_index:].strip()
        name = name[:bank_end_index].strip()  # 截取'**银行'
        full_name = name + branch
        model.tags['branch'] = branch
        model.tags['name'] = name
        model.tags['name:zh'] = name
        model.tags['full_name'] = full_name
        if model.has_diff():
            model.print_diff()
            model.action = 'modify'


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--src',
        default='src.osm',
        help='待处理文件路径'
    )
    argparser.add_argument(
        '--dst',
        default='dst.osm',
        help='处理结果路径'
    )
    argparser.add_argument(
        '--pause',
        default='yes',
        help='运行完成后暂停，yes or no'
    )

    main(argparser.parse_args())

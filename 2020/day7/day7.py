import re

with open('input.txt') as f:
    rules = f.read().splitlines()

bags = {}
for rule in rules:
    bag, inside_bags = rule.split('contain')
    inside_bags = [b.strip() for b in inside_bags.split(',')]
    unrolled_inside_bags = [re.match('(\d)\s([\s\w]+)\s((bags)|(bag))', b) for b in inside_bags]
    unrolled_inside_bags = {m.group(2): int(m.group(1)) for m in unrolled_inside_bags if m}
    bags[bag.split('bags')[0].strip()] = unrolled_inside_bags


def find_bag(bag_name, searched_bag):
    return bag_name == searched_bag or any([find_bag(b, searched_bag) for b in bags[bag_name]])


# part 1
print(sum([any([find_bag(b, 'shiny gold') for b in bags[rule]]) for rule in bags]))


def bag_size(bag_name):
    return sum([bags[bag_name][b] + bags[bag_name][b] * bag_size(b) for b in bags[bag_name]])


# part2
print(sum([bags['shiny gold'][b] + bags['shiny gold'][b] * bag_size(b) for b in bags['shiny gold']]))
